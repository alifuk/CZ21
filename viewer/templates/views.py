from django.shortcuts import render
from viewer.models import Brand, Offer, Comment
# Create your views here.

def landing_page(request):
    return render(
        request, template_name='landing_page.html',
        context={
            "title": "SDAcia",
            "newest_offers": Offer.objects.all(),
            "popular_offers": Offer.objects.all(),
            "newest_comments": Comment.objects.order_by("-commented_date").all()[:10],
            }
    )

def search(request):
    return render(
        request, template_name='search.html',
        context={
            "title": "SDAcia",
            "newest_offers": Offer.objects.all(),
            "popular_offers": Offer.objects.all(),
            "newest_comments": Comment.objects.order_by("-commented_date").all()[:10],
            }
    )

def form_example(request):
    category_name = request.POST.get("category_name", "nothing")
    return render(
        request, template_name='landing_page.html',
        context={"title": "Titulek", "category_name": category_name}
    )

