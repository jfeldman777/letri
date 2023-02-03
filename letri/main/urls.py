from django.urls import path, include
from . import views

urlpatterns = [
#int str path  slug UUID
    path('',views.home,name='home'),
    path('volo',views.volo,name='volo'),
    path('letter',views.letter,name='letter'),
    path('search', views.search,name='search'),
    path('add_body',views.add_body,name='add-body'),
    path('pdf', views.pdf,name='pdf'),
    path('csv', views.csv,name='csv'),
    path('search2', views.search2,name='search2'),
    path('pdf2', views.pdf2,name='pdf2'),
    path('csv2', views.csv2,name='csv2'),
]
