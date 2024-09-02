from django.forms import (
  CharField, DateField, Form, IntegerField, ModelChoiceField, Textarea
)

from viewer.forms import BrandForm
from django.views.generic import FormView

class BrandView(FormView):
  template_name = 'form.html'
  form_class = BrandForm
