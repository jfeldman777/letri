from django.urls import path, include
from . import views

urlpatterns = [
#int str path  slug UUID
    path('',views.home,name='home'),

    path('a',views.a,name='a'),
    path('b',views.b,name='b'),
    path('c',views.c,name='c'),

    #path('s1/<str:name>',views.s1,name='s1'),
    path('s2',views.s2,name='s2'),
    #path('',views.c,name='c'),

    path('volo',views.volo,name='volo'),
    path('letter',views.letter,name='letter'),
    path('search', views.search,name='search'),
    path('add_body',views.add_body,name='add-body'),
    path('pdf', views.pdf,name='pdf'),
    path('csv', views.csv,name='csv'),
    path('all', views.all,name='all'),
    path('about', views.about,name='about'),
    path('pdf2', views.pdf2,name='pdf2'),
    path('csv2', views.csv2,name='csv2'),
    path('s1',views.s1,name='s1'),
]
