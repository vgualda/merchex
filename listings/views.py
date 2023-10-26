from django.http import HttpResponse
from listings.models import Band, Employee
from django.shortcuts import render

def hello(request):
    return HttpResponse("<p>Welcome, mate!</p>")
                  

def about(request):
    employees = Employee.objects.all()
    return render(request, 'listings/about.html',
                  {'employees': employees}
                  )

def listings(request):
    bands = Band.objects.all()
    return render(request, 
                  'listings/hello.html',
                  {'bands': bands}
                  )

def contact(request):
    return render(request, 'listings/contact.html') 