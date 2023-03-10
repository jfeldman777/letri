from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.views.generic import TemplateView, ListView
from .forms import SearchForm1

from django.http import HttpResponseRedirect, HttpResponse
import csv

from .forms import BodyForm,LetterForm, SearchForm
from .models import Body

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter as LETTER

from django.core.paginator import Paginator


def all(request):
    np = request.GET.get('np')
    p = Paginator(Body.objects.filter(flag_done=True), np)
    page = request.GET.get('page')



    bs = p.get_page(page)
    nums = "a"*bs.paginator.num_pages

    return render(request, 'main/pages.html',
        {
        "nums":nums,
        "bs":bs, 'np':np})

def pdf2(request):
    return render(request,'main/home.html')
def about(request):
    return render(request,'main/about.html')

def s1(request,name):

    return render(request,'main/s1.html')

def s2(request):
    qt="";
    qs = Body.objects.filter(flag_done=True)

    region=request.POST.get('region')
    if region!='':
        qt+='// регион = '+region
        qs = qs.filter(region=region)

    army=request.POST.get('army')
    if army!='':
        qt+='// вид войск '+army
        qs = qs.filter(army=army)

    education=request.POST.get('education')
    if education!='':
        qt+='// образование '+education
        sq = qs.filter(education=education)

    mobitype=request.POST.get('mobitype')
    if mobitype!='':
        qt+='// тип мобилизации '+mobitype
        qs = qs.filter(mobitype=mobitype)

    rang=request.POST.get('rang')
    if rang!='':
        qt+='// звание '+rang
        qs = qs.filter(rang=rang)

    ethnos=request.POST.get('ethnos')
    if ethnos!='':
        qt+='// этнос '+ethnos
        qs = qs.filter(ethnos=ethnos)

    birth_date=request.POST.get('birth_date')


    death_date=request.POST.get('death_date')


    count=qs.count()
    return render(request,'main/s.html',{'qt':qt,'count':count})

def s(request):
    p = request.POST.get('np')

    return render(request, 'main/pages.html',
        {
        "nums":nums,
        "bs":bs, 'np':np})


    return render(request,'main/s.html')

def a(request):
    return render(request,'main/a.html')

def b(request):
    return render(request,'main/b.html')

def c(request):
    return render(request,'main/c.html')

def csv2(request):
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

def search3(request):
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


def search(request):
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

def s1(request):
    name = request.POST.get('name','@')
    b_list = Body.objects.filter(last_name__contains=name,flag_done=True)
    return render(request, 'main/s1.html',
        {
            "b_list":b_list,'name':name,
        })


################
from django.shortcuts import render,redirect
import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
import csv as CSV

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
#from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator
import  django.utils.encoding

def csv(request):
    bs = Body.objects.all()
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition']='attachment;filename=data.csv'
    response.write(u'\ufeff'.encode('utf8'))
    writer = CSV.writer(response)

    writer.writerow(['first_name','middle_name','last_name'])
    for b in bs:
        writer.writerow([b.first_name,b.middle_name,b.last_name])
    return response

#from fontTools.ttLib import TTFont

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from letri import settings

def pdf(request):
    pdfmetrics.registerFont(TTFont("Arial", settings.STATICFILES_DIRS[0]+"/arial.ttf"))
    buf = io.BytesIO()
    c = canvas.Canvas(buf,pagesize=LETTER,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)

    #font = TTFont(settings.STATICFILES_DIRS[0]+"/arial.ttf")
    font_name = "Arial"
    textob.setFont(font_name,14)
    #
    bs = Body.objects.all()
    lines = []
    for b in bs:
        lines.append(b.first_name+" "+b.last_name)
        lines.append(" ")

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename="data.pdf",)

# def fetch_pdf_resources(uri, rel):
#     if uri.find(settings.MEDIA_URL) != -1:
#         path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
#     elif uri.find(settings.STATIC_URL) != -1:
#         path = os.path.join(settings.STATIC_ROOT, uri.replace(settings.STATIC_URL, ''))
#     else:
#         path = None
#     return path
