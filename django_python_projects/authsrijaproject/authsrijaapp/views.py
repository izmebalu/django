from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def home_view(request):
    return render(request,'authsrijaapp/home.html')

@login_required
def java_view(request):
    return render(request,'authsrijaapp/javaexams.html')
@login_required
def python_view(request):
    return render(request,'authsrijaapp/pythonexams.html')

def aptitude_view(request):
    return render(request,'authsrijaapp/aptitudeexams.html')