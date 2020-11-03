from django.shortcuts import render

# Create your views here.
def name_view(request):
    return render(request,"gfapp/name.html")

def age_view(request):
    name = request.GET['name'] #fetch the data
    response =  render(request ,"gfapp/age.html")
    response.set_cookie('name',name)#save the data in cookies
    return response

def gf_view(request):
    age = request.GET['age']
    response =  render(request ,"gfapp/gf.html")
    response.set_cookie('age',age)
    return response

def results_view(request):
    gf = request.GET['gf']
    name = request.COOKIES.get('name') #read the data from cookies
    age = request.COOKIES.get('age')
    response =  render(request ,"gfapp/results.html",{'name': name,'age':age,'gf': gf})
    return response



