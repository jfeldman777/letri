from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime
#from .models import Event,Venue

#from .forms import VenueForm, EventForm
from django.http import HttpResponseRedirect, HttpResponse
import csv

from .forms import BodyForm,LetterForm, SearchForm

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator
def pdf(request):
    return render(request,'main/home.html')

def csv(request):
    return render(request,'main/home.html')

def pdf2(request):
    return render(request,'main/home.html')

def csv2(request):
    return render(request,'main/home.html')

def search2(request):
    return render(request,'main/home.html')

def home(request):
    return render(request,'main/home.html')

def volo(request):
    return render(request,'main/volo.html')

def search(request):
    return render(request,'main/search.html')

def letter(request):
    submitted = False
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/letter?submitted=True')
    else:
        form = LetterForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'main/letter.html',
    {'form':form,
    'submitted':submitted,})


def search3(request):
    submitted = False
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/search?submitted=True')
    else:
        form = SearchForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'main/search.html',
    {'form':form,
    'submitted':submitted,})

def add_body(request):
    submitted = False
    form = BodyForm

    if request.method == "POST":
        form = BodyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_body?submitted=True')
    else:
        form = BodyForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'main/add_body.html',
    {'form':form,
    'submitted':submitted,})
