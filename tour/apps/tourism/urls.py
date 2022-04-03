from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path('order-room/', OrderRoomView.as_view(), name='room_order')
]
