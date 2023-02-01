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

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator

def home(request):
    return render(request,'main/home.html')
