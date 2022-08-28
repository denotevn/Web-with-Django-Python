from email import message
from multiprocessing import context
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, redirect # chuyen huong sang trang khac neu thoa man dieu kien
from django.contrib.auth.models import User, auth
from django.contrib import messages
# for login
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this

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

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already exits')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already Used. Please choose another name.') 
                return redirect('register')
            else:
                user = User.objects.create_user(username, email, password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password Not The Same')
            return redirect('register')
    else:
        # save data to database
        return render(request, 'register.html')   

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            message.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    # text = request.POST['text'] # text is nametype of <form .... in index.html
    # amount_of_word = len(text.split())
    ## Sau khi tinh xong thi can gui thang "amount_of_words" vao file "counter.html"
    posts = [1,2,3,4,5,'Tuan','admin'] 
    # Giai quy van de Url Routing cho ca str va int

    return render(request, 'counter.html', {'posts':posts})

def post(request,pk):
    return render(request, 'post.html', {'pk':pk})