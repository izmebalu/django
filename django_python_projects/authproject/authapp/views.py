from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage_view(request):
    return render(request,'authapp/home.html')
@login_required
def java_view(request):
    return render(request,'authapp/javaexams.html')

def python_view(request):
    return render(request,'authapp/pythonexams.html')

def aptitude_view(request):
    return render(request,'authapp/aptitudeexams.html')