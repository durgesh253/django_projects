from django.urls import path
from .views import *

urlpatterns = [
   path("", Index,name="todo"),
   path("del/<str:item_id>",Remove, name="del"),
]
