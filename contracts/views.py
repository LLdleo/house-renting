from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Contract
from contacts.models import Contact
from listings.models import Listing


def contract_create(request):
    """
    add new unsigned contract into contracts and change contact to replied
    :param request:
    :return:
    """
    if request.method == 'POST':
        listing_id = request.POST['listing_id1']
        user_id = request.POST['the_user_id']
        manager_id = request.POST['manager_id2']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        message = request.POST['reply_message']

        contact_id = request.POST['contact_id']

        contract = Contract(listing_id=listing_id, user_id=user_id, manager_id=manager_id, start_date=start_date, end_date=end_date)
        contract.save()
        Contact.objects.filter(id=contact_id).update(replied=True, reply_message=message)

        messages.success(request, 'New contract has been created, and your reply has also been sent')
        return redirect('/accounts/dashboard')


def contract_deny(request):
    if request.method == 'POST':
        message = request.POST['leave_a_message']
        contact_id = request.POST['contact_id1']

        Contact.objects.filter(id=contact_id).update(replied=True, reply_message=message, closed=True)

        return redirect('/accounts/dashboard')


def contract_sign(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['sign_date']
        contract_id = request.POST['contract_id']

        listing_id = Contract.objects.filter(id=contract_id).values_list('listing_id').first()[0]
        max_capacity = Listing.objects.filter(id=listing_id).values_list('bedrooms').first()[0]
        print('max_capacity', max_capacity)
        current_occupied = Contract.objects.filter(listing_id=listing_id, valid=True).count()
        print('current_occupied', current_occupied)
        if current_occupied < max_capacity:
            Listing.objects.filter(id=listing_id).update(current_occupied=current_occupied+1)
            Contract.objects.filter(id=contract_id).update(if_signed=True, valid=True, sign_name=name, sign_date=date)

        return redirect('/accounts/dashboard')


def contract(request, contract_id):
    contract_info = get_object_or_404(Contract, pk=contract_id)

    context = {
        'contract': contract_info
    }

    return render(request, 'contracts/contract.html', context)


def end_contract(request):
    if request.method == 'POST':
        contract_id = request.POST['contract_id1']
        import datetime
        dt = datetime.datetime.now()
        today = '-'.join([str(dt.year), str(dt.month), str(dt.day)])

        Contract.objects.filter(id=contract_id).update(valid=False, end_date=today)

        return redirect('/accounts/dashboard')
