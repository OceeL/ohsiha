from __future__ import unicode_literals
import requests
from operator import itemgetter
from collections import Counter
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from extendflix.models import Movie

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('login')

    movies_data = []
    movies = Movie.objects.all()

    for movie in movies:
        movie_data = {
            'movie_name': movie.movie_name,
            'movie_image': movie.image,
            'movie_released': movie.released,
            'movie_runtime': movie.runtime,
            'movie_imdb_id': movie.imdb_id,
            'movie_imdb_rating': movie.imdb_rating,
            'movie_rotten_tomatoes_rating': movie.rotten_tomatoes_rating,
            'movie_metacritic_rating': movie.metacritic_rating,
        }
        movies_data.append(movie_data)

    context = {'movies_data': movies_data}

    return render(request, 'extendflix/index.html', context)


def data_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    imbd_rating_ids = Movie.objects.exclude(imdb_rating="").values_list('imdb_rating')
    rottentomato_rating_ids = Movie.objects.exclude(rotten_tomatoes_rating="").values_list('rotten_tomatoes_rating')
    metacritic_rating_ids = Movie.objects.exclude(metacritic_rating="").values_list('metacritic_rating')


    imdb_ratings = list(map(itemgetter(0), imbd_rating_ids))
    imdb_ratings = [s.strip('/10') for s in imdb_ratings]
    imdb_ratings = [int(float(x)) for x in imdb_ratings]
    imdb_ratings = Counter(imdb_ratings)

    rottentomato_ratings = list(map(itemgetter(0), rottentomato_rating_ids))
    rottentomato_ratings = [s.strip('%') for s in rottentomato_ratings]
    rottentomato_ratings = [int(float(x)/10) for x in rottentomato_ratings]
    rottentomato_ratings = Counter(rottentomato_ratings)

    metacritic_ratings = list(map(itemgetter(0), metacritic_rating_ids))
    metacritic_ratings = [s.replace('/100','') for s in metacritic_ratings]
    metacritic_ratings = [int(float(x)/10) for x in metacritic_ratings]
    metacritic_ratings = Counter(metacritic_ratings)

    ratings_list = [imdb_ratings, rottentomato_ratings, metacritic_ratings]

    for n in range(0, 3):
        labels = [0] * 10
        for i in range(0, 9):
            if ratings_list[n][i+1]:
                labels[i] = ratings_list[n][i+1]

        ratings_list[n] = labels
    print(ratings_list)

    ratings = {'imdb':ratings_list[0], 'rotten_tomato': ratings_list[1], 'metacritic':ratings_list[2]}

    context = {'movies_data': ratings}

    return render(request, 'extendflix/data_page.html', context)

def get_ratings(imdbid):

    url = 'http://www.omdbapi.com/'
    api_key = 'dd493a12'
    imdb_id = imdbid
    url = '{0}?i={1}&apikey={2}'.format(url, imdb_id, api_key)

    imdb_rating = ''
    rotten_tomatoes_rating = ''
    metacritic_rating = ''

    try:
        response = requests.request("GET", url)
        response = response.json()
        ratings = response['Ratings']

        for rating in ratings:
            if rating['Source'] == 'Internet Movie Database':
                imdb_rating = rating['Value']
            elif rating['Source'] == 'Rotten Tomatoes':
                rotten_tomatoes_rating = rating['Value']
            elif rating['Source'] == 'Metacritic':
                metacritic_rating = rating['Value']

        return(imdb_rating,rotten_tomatoes_rating,metacritic_rating)

    except:
        return (imdb_rating, rotten_tomatoes_rating, metacritic_rating)


def update_movies():
    # uNoGs API-request
    url = "https://unogs-unogs-v1.p.rapidapi.com/aaapi.cgi"

    querystring = {"q": "get:new7:US", "p": "1", "t": "ns", "st": "adv"}

    headers = {
        'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com",
        'x-rapidapi-key': "cd850b63f1msh0e38b5b9590e726p1b0bd7jsn13eade9e5b15"
    }

    Movie.objects.all().delete()

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        response = response.json()

        # Getting the movies data and going thourgh it
        movies = response['ITEMS']
        print(response['ITEMS'])

        for movie in movies:

            new_movie = Movie()
            new_movie.movie_name = movie['title']
            new_movie.image = movie['image']
            new_movie.released = movie['released']
            new_movie.runtime = movie['runtime']
            new_movie.imdb_id = movie['imdbid']
            # Cheking the ratings for the movie
            print(movie['title'])
            print(movie['imdbid'])
            if movie['imdbid'] and movie['imdbid'] != 'notfound':
                imdb_rating,rotten_tomatoes_rating,metacritic_rating = get_ratings(movie['imdbid'])
                new_movie.imdb_rating = imdb_rating
                new_movie.rotten_tomatoes_rating = rotten_tomatoes_rating
                new_movie.metacritic_rating = metacritic_rating

                print(imdb_rating)
                print(rotten_tomatoes_rating)
                print(metacritic_rating)

            print("Saving movie " + movie['title'])
            new_movie.save()

    except:
        print("Something went wrong")
        return


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
