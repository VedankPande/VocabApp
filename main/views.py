from django.shortcuts import render
from django.views import View
from main.models import Words
from django.http import JsonResponse
import random

# Create your views here.

def home(response,id):
    record = Words.objects.filter(id=id).first()
    return render(response,'main.html',{'id':id,'record':record})

def next(response):
    id = int(response.GET.get('id',None))
    print("id received",id)
    record = Words.objects.filter(id = id+1).first()
    print(record.word)
    data = {
        'id': record.id,
        'word' : record.word,
        'meaning' : record.meaning
    }

    return JsonResponse(data)

def prev(response):
    id = int(response.GET.get('id',None))
    print("id received",id)
    record = Words.objects.filter(id = id-1).first()
    print(record.word)
    data = {
        'id': record.id,
        'word' : record.word,
        'meaning' : record.meaning
    }


    return JsonResponse(data)

def rand(response):
    id = random.randint(1,262)
    record = Words.objects.filter(id=id).first()
    data = {
        'id': record.id,
        'word' : record.word,
        'meaning' : record.meaning
    }

    return JsonResponse(data)