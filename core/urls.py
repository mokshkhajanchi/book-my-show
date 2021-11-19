from django.urls import path, include
from . import views

urlpatterns = [
    path('core/movies_as_per_city/', views.MovieView.as_view({
        'post': 'get_movies_as_per_city'
    }), 
    name='get-movies-as-per-city'),
    path('core/cinemas_as_per_movie/', views.MovieView.as_view({
        'post': 'get_cinemas_as_per_movie'
    }), 
    name='get-cinemas-as-per-movie'),
    path('core/seats_as_per_showtime/', views.MovieView.as_view({
        'post': 'get_seats_as_per_showtime'
    }), 
    name='get-seats-as-per-showtime'),
    path('core/reserve_tickets/', views.ReservationView.as_view({
        'post': 'reserve_tickets'
    }), 
    name='reserve-tickets'),
]