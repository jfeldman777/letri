from django.urls import path, include
from . import views

urlpatterns = [
#int str path  slug UUID
    path('',views.home,name='home'),
    path('volo',views.volo,name='volo'),
    path('letter',views.letter,name='letter'),
    path('search', views.search,name='search'),
    path('add_body',views.add_body,name='add-body'),
]
