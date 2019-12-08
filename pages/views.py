from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, room_choices, property_types

from listings.models import Listing
from managers.models import Manager


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'property_type': property_types,
        'room_choices': room_choices,
        'price_choices': price_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):
    # Get all managers
    managers = Manager.objects.order_by('-hire_date')

    # Get MVP
    mvp_managers = Manager.objects.all().filter(is_mvp=True)

    context = {
        'managers': managers,
        'mvp_managers': mvp_managers
    }

    return render(request, 'pages/about.html', context)
