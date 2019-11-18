from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact
from contracts.models import Contract
from .models import Profile
from managers.models import Manager


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        dateOfBirth = request.POST['dateOfBirth']
        phoneNumber = request.POST['phoneNumber']
        faculty = request.POST['faculty']
        academicYear = request.POST['academicYear']
        gender = request.POST['gender']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password,email=email, first_name=first_name, last_name=last_name)
                    profile = Profile(user=user, dateOfBirth=dateOfBirth, phoneNumber=phoneNumber, faculty=faculty,
                                      academicYear=academicYear, gender=gender)
                    profile.save()
                # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    messages.success(request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
            # a = User.objects.filter(username=username, is_staff='1')
            # print(len(a))
            # if len(a) == 1:
            #     return redirect('manager_board')
            # else:
            #     return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')


def dashboard(request):
    a = User.objects.filter(id=request.user.id, is_staff='1')
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    if len(a) != 1:
        contracts = Contract.objects.filter(user_id=request.user.id).order_by('-start_date')
        context = {
            'contacts': user_contacts,
            'contracts': contracts
        }
        return render(request, 'accounts/dashboard.html', context)
    else:
        manager_id = Manager.objects.get(user_id=request.user.id)
        manager_contacts = Contact.objects.order_by('contact_date').filter(manager_id=manager_id)
        contracts = Contract.objects.filter(manager_id=manager_id).order_by('-id')
        context = {
            'contacts': user_contacts,
            'manager_contacts': manager_contacts,
            'contracts': contracts
        }
        return render(request, 'accounts/manager_board.html', context)
