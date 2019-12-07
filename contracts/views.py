from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .models import Contract
from contacts.models import Contact


def contract_create(request):
    """
    add new unsigned contract into contracts and change contact to replied
    :param request:
    :return:
    """
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        user_id = request.POST['the_user_id']
        manager_id = request.POST['manager_id']
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
        message = request.POST['message']
        contact_id = request.POST['contact_id']

        Contact.objects.filter(id=contact_id).update(replied=True, reply_message=message, closed=True)

        return redirect('/accounts/dashboard')


def contract_sign(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['sign_date']
        contract_id = request.POST['contract_id']

        Contract.objects.filter(id=contract_id).update(if_signed=True, valid=True, sign_name=name, sign_date=date)

        return redirect('/accounts/dashboard')


def contract(request, contract_id):
    contract_info = get_object_or_404(Contract, pk=contract_id)

    context = {
        'contract': contract_info
    }

    return render(request, 'contracts/contract.html', context)
