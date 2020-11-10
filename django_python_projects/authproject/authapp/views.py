from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import SignupForm
from django.http import HttpResponseRedirect
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

def logout_view(request):
    return render(request,'authapp/logout.html')

def signup_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form=SignupForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'authapp/signup.html',{'form':form})