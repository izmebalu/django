from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def without_rest(request):
    emp_view={
        'name': 'bharath',
        'age': 29,
        'domain': 'Devops',
        'sal': 250000,
        'addr': 'hyderabad'
    }

    resp ='<h1>Employee name: {}<br>Employee age: {}<br>Employee domain: {}<br>Employee salary: {}<br>Employee address: {}<br></h1>'.format(emp_view['name'],emp_view['age'],emp_view['domain'],emp_view['sal'],emp_view['addr'])
    return HttpResponse(resp)

import json
def without_rest_json(request):
    emp_view={
        'name': 'bharath',
        'age': 29,
        'domain': 'Devops',
        'sal': 250000,
        'addr': 'hyderabad'
    }

    json_data = json.dumps(emp_view)
    return HttpResponse(json_data, content_type = 'application/json')

from django.http import JsonResponse
def without_rest_json2(request):
    emp_view={
        'name': 'bharath',
        'age': 29,
        'domain': 'Devops',
        'sal': 250000,
        'addr': 'hyderabad'
    }

    return JsonResponse(emp_view)