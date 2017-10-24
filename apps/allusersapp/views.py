# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from models import *
from django.core import serializers
# Create your views here.
def index(request):
    response="test"
    return render(request,'allusersapp/index.html')

def all_json(request):
    users=User.objects.all()
    users_json=serializers.serialize("json",users)
    print users_json
    return HttpResponse(users_json, content_type='application/json')

def all_html(request):
    users=User.objects.all()
    context={'user':users}
    return render(request,"allusersapp/userAll.html",context)

def find(request):
    users=User.objects.filter(first_name__startswith=request.POST['name_starts'])
    context={'user':users}
    print users
    return render(request,'allusersapp/userAll.html',context)

def add(request):
    fname=request.POST['fnameTA']
    lname=request.POST['lnameTA']
    email=request.POST['emailTA']
    age=request.POST['ageTA']
    User.objects.create(first_name=fname,last_name=lname,email=email,age=age)
    users=User.objects.all()
    context={'user':users}
    return render(request,"allusersapp/userAll.html",context)
