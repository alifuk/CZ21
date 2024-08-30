from django.shortcuts import render
from viewer.models import Brand, Offer, Comment, VehicleType
# Create your views here.

def landing_page(request):
    return render(
        request, template_name='landing_page.html',
        context={
            "title": "SDAcia",
            "newest_offers": Offer.objects.order_by("-offer_date").all()[:5],
            "popular_offers": Offer.objects.order_by("-view_count").all()[:5],
            "newest_comments": Comment.objects.order_by("-commented_date").all()[:5],
            }
    )

def offer(request, pk_offer):
    offer = Offer.objects.get(pk=pk_offer)
    offer.view_count += 1
    offer.save()
    return render(
        request, template_name='offer.html',
        context={
            "title": "SDAcia",
            "offer": offer,
            "comments": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all(),
            "comments_count": Comment.objects.filter(offer__pk=pk_offer).order_by("-commented_date").all().count()
            }
    )

def search(request):

    filtered_offers = Offer.objects.all()

    filter_of_description = request.GET.get("search_description", "")
    if filter_of_description != "":
        filtered_offers = filtered_offers.filter(description__contains=filter_of_description)

    filter_of_brand = request.GET.get("search_brand", "")
    if filter_of_brand != "":
        filtered_offers = filtered_offers.filter(brand__pk=filter_of_brand)

    filter_of_price_from = request.GET.get("search_price_from", "")
    if filter_of_price_from != "":
        filtered_offers = filtered_offers.filter(price__gt=filter_of_price_from)

    filter_of_price_to = request.GET.get("search_price_to", "")
    if filter_of_price_to != "":
        filtered_offers = filtered_offers.filter(price__lt=filter_of_price_to)

    filter_of_type= request.GET.get("search_type", "")
    if filter_of_type != "":
        filtered_offers = filtered_offers.filter(vehicle_type__pk=filter_of_type)

    filter_of_year_from = request.GET.get("search_year_from", "")
    if filter_of_year_from != "":
        filtered_offers = filtered_offers.filter(year__gt=filter_of_year_from)

    filter_of_year_to = request.GET.get("search_year_to", "")
    if filter_of_year_to != "":
        filtered_offers = filtered_offers.filter(year__lt=filter_of_year_to)

    

    
    return render(
        request, template_name='search.html',
        context={
            "title": "Hledat",
            "offers": filtered_offers,
            "all_brands": Brand.objects.all(),
            "all_types": VehicleType.objects.all()
            }
    )

def form_example(request):
    category_name = request.POST.get("category_name", "nothing")
    return render(
        request, template_name='landing_page.html',
        context={"title": "Titulek", "category_name": category_name}
    )


def add_offer(request):
    status = ""
    if "description" in request.POST:
        brand = request.POST.get("brand", "")
        vehicle_type = request.POST.get("type", "")
        
        new_offer = Offer()
        new_offer.description = request.POST.get("description", "")
        new_offer.price = int(request.POST.get("price", 0) )
        new_offer.year = int(request.POST.get("year", 0) )
        new_offer.power = int(request.POST.get("power", 0) )
        new_offer.brand = Brand.objects.get(pk=brand)
        new_offer.vehicle_type = VehicleType.objects.get(pk=vehicle_type)
        new_offer.save()
        status = "Přidáno"
        pass


    return render(
        request, template_name='add_offer.html',
        context={
            "title": "Přidat inzerát",
            "all_brands": Brand.objects.all(),
            "all_types": VehicleType.objects.all(),
            "status": status
            }
    )

def add_comment(request):
    pk_offer = request.POST.get("pk_offer")
    new_comment = Comment()
    new_comment.offer = Offer.objects.get(pk=pk_offer)
    new_comment.username = request.POST.get("username", "Nikdo")
    new_comment.text = request.POST.get("text", "Bez textu")
    new_comment.save()
    return offer(request, pk_offer)