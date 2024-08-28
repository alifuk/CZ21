from django.shortcuts import render

# Create your views here.

def landing_page(request):
    return render(
        request, template_name='landing_page.html',
        context={"title": "Titulek"}
    )

def form_example(request):
    category_name = request.POST.get("category_name", "nothing")
    return render(
        request, template_name='landing_page.html',
        context={"title": "Titulek", "category_name": category_name}
    )

