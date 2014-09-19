from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
import time
from movie_mapper.forms import SimpleInput
from movie_mapper.models import Movie, Location
from imdb import IMDb
import urllib2
from bs4 import BeautifulSoup
from pygeocoder import Geocoder



def get_locations(movie):
    link = 'http://www.imdb.com/title/tt{}/locations'.format(movie.movie_id)
    page = urllib2.urlopen(link).read()
    soup = BeautifulSoup(page)
    soup.prettify()
    locations = []
    for link in soup.find_all(itemprop='url'):
        locations.append(link.get_text())
    for location in locations[1:]:
        if not Location.objects.filter(place=location):
            geocode = Geocoder.geocode(location)
            coordinates = geocode[0].coordinates
            site = Location.objects.create(place=location, longitude=coordinates[0], latitude=coordinates[1])
            site.save()
            site.movies.add(movie)
            time.sleep(0.11)
        else:
            spot = Location.objects.get(place=location)
            spot.movies.add(movie)
    movie.searched = True
    movie.save()
    # return locations[1:]


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.save()
            # wallet = Wallet(player=user, balance=1000)
            # wallet.save()
            # text_content = 'Thank you for signing up for our website, {} {}'.format(user.first_name, user.last_name)
            # html_content = '<h2>Thanks {} {} for signing up!</h2> <div>I hope you enjoy using our site</div>'.format(user.first_name, user.last_name)
            # msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            # msg.attach_alternative(html_content, "text/html")
            # msg.send()
            return redirect("profile")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })


@login_required
def profile(request):
    return render(request, 'profile.html')


def test(request):
    return render(request, 'test.html')


def movie_list(request):
    movies = request.user.movies.all()
    data = {
        'movies': movies
    }
    return render(request, 'movie_list.html', data)


def location_list(request):
    return render(request, 'location_list.html')


def search_movie(request):
    data = {"search_movie_form": SimpleInput(), }
    if request.method == "POST":
        form = SimpleInput(request.POST)
        if form.is_valid():
            ia = IMDb()
            movies = ia.search_movie(form.cleaned_data['question'])
            data = {
                'movies': movies
            }
            return render(request, "show_movie.html", data)
        else:
            data = {"search_movie_form": form, }
    return render(request, "search_movie.html", data)


def add_movie(request):
    data = {"add_movie_form": SimpleInput(), }
    if request.method == "POST":
        form = SimpleInput(request.POST)
        if form.is_valid():
            ia = IMDb()
            movie_info = ia.get_movie(form.cleaned_data['question'])
            if Movie.objects.filter(movie_id=movie_info.movieID):       # if movie in our Db
                movie = Movie.objects.get(movie_id=movie_info.movieID)
                movie.user.add(request.user)
                if not movie.searched:                                  # if movie has not been searched, scrape locations
                    get_locations(movie)
            else:                                                       # if movie not in our Db add it and scrape locations
                movie = Movie.objects.create(title=movie_info['title'], movie_id=movie_info.movieID)
                movie.save()
                movie.user.add(request.user)
                get_locations(movie)
            redirect("/movies/")
        else:
            data = {"add_movie_form": form, }
    return render(request, "add_movie.html", data)


def add_location(request):
    return render(request, 'add_location.html')


def map_view(request, movie_id):
    spots = []
    for place in Location.objects.filter(movies__movie_id=movie_id):
        spots.append([place.longitude, place.latitude])
    data = {
        'spots': spots
    }
    return render(request, 'map_view.html', data)


def faq(request):
    return render(request, 'faq.html')