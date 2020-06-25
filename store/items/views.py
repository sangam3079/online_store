from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Item

from django.views.generic import TemplateView,ListView
class IndexView(TemplateView):
    template_name = 'project.html'

class DisplayView(ListView):
    modal = Item
    template_name='display.html'

    def get_queryset(self, **kwargs):
        object_list = Item.objects.all
        return object_list
     
class PaymentView(TemplateView):
    template_name = 'payment.html'




