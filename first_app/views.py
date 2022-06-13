from django.shortcuts import render
from django.http import HttpResponse
from . import models 
from .models import Destination

############
from django.shortcuts import redirect
# Create your views here


# Define home function

def home(request):
    #return HttpResponse("<h1> old </h1>")
    #return render(request,'base.html')
    return render(request,'home.html',{'name':'FARES'})


def add(request):

    val1 = int(request.POST['num1'])

    val2 = int(request.POST['num2'])

    res = val1 + val2

    return render (request,'result.html',{'result':res})


def index(request):
    
    #dest1 = models.Destination()
    #dest1.name = 'Mubai'
    #dest1.desc='The City That Never Sleep!'
    #dest1.img='destination_1.jpg'
    #dest1.price=3400
    #dest1.offer=True

    #dest2 = models.Destination()
    #dest2.name = 'Hyderabad'
    #dest2.desc='First Biryani, Then Sherwani'
    #dest2.img='destination_2.jpg'
    #dest2.price=2650
    #dest2.offer=False

    #dest3 = models.Destination()
    #dest3.name = 'Bengaluru'
    #dest3.desc='Beautiful City'
    #dest3.img='destination_3.jpg'
    #dest3.price=1750
    #dest3.offer=False

    #dest4 = models.Destination()
    #dest4.name = 'pares'
    #dest4.desc='The City That Never Sleep!'
    #dest4.img='destination_4.jpg'
    #dest4.price=7600
    #dest4.offer=False

    #dest5 = models.Destination()
    #dest5.name = 'V_City'
    #dest5.desc='First Biryani, Then Sherwani'
    #dest5.img='destination_5.jpg'
    #dest5.price=6500
    #dest5.offer=True

    #dest6 = models.Destination()
    #dest6.name = 'Nables'
    #dest6.desc='Beautiful City'
    #dest6.img='destination_6.jpg'
    #dest6.price=1850
    #dest6.offer=True

    #dests=[dest1,dest2,dest3,dest4,dest5,dest6]

    #return render (request,'index.html', {'dests':dests})
    ############################################################
    ######## NOW READ DATA FRO DB
    dests=Destination.objects.all()
    return render (request,'index.html', {'dests':dests})


###############################
def add1(request):
    #return render(request,'home.html')
    obj = MyModel.objects.get()
    return redirect(obj)