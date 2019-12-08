from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        property_name = request.POST['property_name']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        manager_id = request.POST['manager_id']
        manager_email = request.POST['manager_email']

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id, closed=False)
            if len(has_contacted) > 0:
                messages.error(request, 'You have already made an inquiry for this property')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=property_name, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id, manager_id=manager_id)

        contact.save()

        # Send email
        # send_mail(
        #   'Property Listing Inquiry',
        #   'There has been an inquiry for ' + listing + '. Sign into the admin panel for more info',
        #   'traversy.brad@gmail.com',
        #   [manager_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted, a manager will get back to you soon')
        return redirect('/listings/'+listing_id)
