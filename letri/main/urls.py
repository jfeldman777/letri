from django.urls import path, include
from . import views

urlpatterns = [
#int str path  slug UUID
    path('',views.home,name='home'),
    path('add_body',views.add_body,name='add-body'),
]
