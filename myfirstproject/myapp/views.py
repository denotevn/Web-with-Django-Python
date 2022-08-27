from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
   return render(request, 'login.html')

def index(request):
    context = {
        'name':'Tuan Dinh',
        'age':23,
        'nationality':'VietNam',
    }

    return render(request,'index.html', context)