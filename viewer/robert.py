from django.views.generic import TemplateView
from django.views.generic import ListView
from viewer.models import Comment, Brand

class RobertTemplateView(TemplateView):
    template_name = 'robert.html'
    extra_context = {
        "vek": 25,
        "jeden_komentar": Comment.objects.first()
    }


class CarsView(ListView):
  template_name = 'cars.html'
  model = Brand