from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapp.models import Contact



# Create your views here.
def about(request):
    return render(request, "about.html")
    #return HttpResponse("this is about page")

def index(request):
    return render(request, "index.html")
    #return HttpResponse("this is home page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact = Contact(name="name", email="email",phone="phone", desc="desc", date=datetime.today())
        contact.save()
    return render(request, "contact.html")
    #return HttpResponse("this is contact page")

def NOM_details(request):
    return render(request, "NOM_details.html")

def Femto_small_cells(request):
    return render(request, "Femto_small_cells.html")