from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login(request):
   return render(request, 'login.html')

def index(request):
    return render(request,'index.html')

def counter(request):
    text = request.POST['text'] # text is nametype of <form .... in index.html
    amount_of_word = len(text.split())
    ## Sau khi tinh xong thi can gui thang "amount_of_words" vao file "counter.html"
    return render(request, 'counter.html', {'amount':amount_of_word})