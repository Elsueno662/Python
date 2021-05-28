from django.views.generic import TemplateView
from .models import Product


class HomePageView(TemplateView):
    template_name = 'home.html'
    extra_context = {'prod': Product.objects.all()}
