from django.urls import path

from . import views
from items.views import IndexView, DisplayView, PaymentView

urlpatterns = [
    path('', IndexView.as_view(), name='project'),
    path('display/', DisplayView.as_view(), name='display'), 
    path('payment/', PaymentView.as_view(), name='payment')
]