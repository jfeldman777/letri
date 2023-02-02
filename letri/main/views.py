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

from .forms import BodyForm

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator

def home(request):
    return render(request,'main/home.html')

def add_body(request):
    submitted = False
    if request.method == "POST":
        form = BodyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_body?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'main/add_body.html',
    {'form':form,
    'submitted':submitted,})
