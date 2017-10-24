# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect, HttpResponse
from models import *
from django.core import serializers
# Create your views here.
def index(request):
    notes=Note.objects.all()
    context={'notes':notes}
    return render(request,'notes/index.html',context)

def add(request):
    noteTA=request.POST['noteTA']
    Note.objects.create(note=noteTA)
    notes=Note.objects.all()
    context={'notes':notes}
    return render(request,'notes/newNote.html',context)

def delete(request):
    noteTD=Note.objects.get(id=request.POST['id'])
    noteTD.delete()
    print noteTD.note
    notes=Note.objects.all()
    context={'notes':notes}
    print notes
    return render(request,'notes/newNote2.html',context)

def refresh(request):
    notes=Note.objects.all()
    context={'notes':notes}
    return render(request,'notes/newNote.html',context)
