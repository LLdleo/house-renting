from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, room_choices, property_types, energy_list, hot_water_list, heating_list, furnished_list

from .models import Listing
from contacts.models import Contact


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    contact_info = Contact.objects.filter(listing_id=page)

    context = {
        'listings': paged_listings,
        'contact_info': contact_info
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    list_ = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': list_
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    # Address
    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list = queryset_list.filter(address__icontains=address)

    # house_type
    if 'property_type' in request.GET:
        house_type = request.GET['property_type']
        if house_type:
            queryset_list = queryset_list.filter(house_type__exact=house_type)

    # energy
    if 'energy' in request.GET:
        energy = request.GET['energy']
        if energy:
            queryset_list = queryset_list.filter(energy__exact=energy)

    # hot_water
    if 'hot_water' in request.GET:
        hot_water = request.GET['hot_water']
        if hot_water:
            queryset_list = queryset_list.filter(hot_water__exact=hot_water)

    # heating
    if 'heating' in request.GET:
        heating = request.GET['heating']
        if heating:
            queryset_list = queryset_list.filter(heating__exact=heating)

    # furnished
    if 'furnished' in request.GET:
        furnished = request.GET['furnished']
        if furnished:
            queryset_list = queryset_list.filter(furnished__exact=furnished)

    context = {
        'property_types': property_types,
        'bedroom_choices': room_choices,
        'price_choices': price_choices,
        'energy_list': energy_list,
        'hot_water_list': hot_water_list,
        'heating_list': heating_list,
        'furnished_list': furnished_list,
        'listings': queryset_list,
        'values': request.GET
    }

    return render(request, 'listings/search.html', context)
