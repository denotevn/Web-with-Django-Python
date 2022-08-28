from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# When you cretaed model in models.py you can import it here
from .models import Feature

# Create your views here.

def index(request):
    '''
    Because we use database, this code should delete

    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quickly'
    '''
    # with manage from databse:
    # This features nahn du lieu tu du lieu quan ly cua admin.
    features = Feature.objects.all()

    return render(request,'index.html', {'features':features})


def login(request):
   return render(request, 'login.html')

def counter(request):
    text = request.POST['text'] # text is nametype of <form .... in index.html
    amount_of_word = len(text.split())
    ## Sau khi tinh xong thi can gui thang "amount_of_words" vao file "counter.html"
    return render(request, 'counter.html', {'amount':amount_of_word})