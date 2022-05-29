from django.shortcuts import render
from django.http import HttpResponse


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






###############################3
def add1(request):
    #return render(request,'home.html')
    obj = MyModel.objects.get()
    return redirect(obj)