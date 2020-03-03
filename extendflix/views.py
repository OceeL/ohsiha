from __future__ import unicode_literals
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.




def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    print("Tuleeko alle tervehdystä")
    return render(request, 'extendflix/index.html')


def update_movies():
    # Testi alkaa
    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q": "get:new7:US", "p": "1", "t": "ns", "st": "adv"}

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': "cd850b63f1msh0e38b5b9590e726p1b0bd7jsn13eade9e5b15"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)


    #print(response.text)
    response = response.json()
    #print(response)
    #print(response['ITEMS'])
    movies = response['ITEMS']
    for movie in movies:
        print(movie['title'])


def register(request):
    if request.method == 'post':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            redirect('index')
    else:
        form = UserCreationForm()
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
