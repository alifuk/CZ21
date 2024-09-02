"""SDAcia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from viewer.views import landing_page, form_example, search, add_offer, offer, add_comment
from viewer.models import Brand, Comment, Offer, VehicleType
from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

class LandingView(View):
  def get(self, request):
    return render(
        request, template_name='landing_page.html',
        context={
            "title": "SDAcia",
            "newest_offers": Offer.objects.order_by("-offer_date").all()[:5],
            "popular_offers": Offer.objects.order_by("-view_count").all()[:5],
            "newest_comments": Comment.objects.order_by("-commented_date").all()[:5],
            }
    )

class LandingTemplateView(TemplateView):
  template_name = 'landing_page.html'
  extra_context = {
            "title": "SDAcia",
            "newest_offers": Offer.objects.order_by("-offer_date").all()[:5],
            "popular_offers": Offer.objects.order_by("-view_count").all()[:5],
            "newest_comments": Comment.objects.order_by("-commented_date").all()[:5],
            }

admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Offer)
admin.site.register(VehicleType)

from viewer.robert import RobertTemplateView, CarsView

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', landing_page, name="landing_page"), #Pohled založený na funkci
    #path('', LandingView.as_view(), name="landing_page"), #Pohled založený na třídě dědící View
    path('', LandingTemplateView.as_view(), name="landing_page"), #Pohled založený na třídě dědící TemplateView
    #path('search', search),
    path('search/', search),
    path('my_first_form', form_example),
    path('my_first_form/', form_example),
    path('add_offer', add_offer, name="add_offer"),
    path('add_offer/', add_offer),
    path('add_comment', add_comment),
    path('add_comment/', add_comment),
    path('offer/<pk_offer>', offer, name='offer'),  # http://127.0.0.1:8000/offer/6   <a href="/offer/{{offer.pk}}">Detail</a></p>
    path('robert', RobertTemplateView.as_view() ), 
    path('cars_view', CarsView.as_view() ),
    
    
]
