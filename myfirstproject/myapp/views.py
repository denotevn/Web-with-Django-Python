from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# When you cretaed model in models.py you can import it here
from .models import Feature

# Create your views here.

def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our service is very quickly'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy To Use'
    feature3.is_true = False
    feature3.details = 'Our service is very easy to use'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.is_true = True
    feature4.details = 'Our service is very affortable'

    # Create and then views will quickly code with loop
    features = [feature1, feature2, feature3, feature4]

    return render(request,'index.html', {'features':features})



def login(request):
   return render(request, 'login.html')

def counter(request):
    text = request.POST['text'] # text is nametype of <form .... in index.html
    amount_of_word = len(text.split())
    ## Sau khi tinh xong thi can gui thang "amount_of_words" vao file "counter.html"
    return render(request, 'counter.html', {'amount':amount_of_word})