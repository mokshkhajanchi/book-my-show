from typing import Tuple
from django.contrib import admin
from .models import Movie, Cinema, CinemaSeat, Reservation, Showtime

@admin.register(Movie)
class MovieModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'duration', 'release_date']

@admin.register(Cinema)
class CinemaModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'total_seats', 'city']

@admin.register(CinemaSeat)
class CinemaSeatModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'available_seats', 'showtime']

@admin.register(Reservation)
class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'showtime', 'number_of_seats', 'status']

@admin.register(Showtime)
class ShowtimeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'start_time', 'end_time', 'get_movie_title', 'get_cinema_name']

    def get_cinema_name(self, obj):
        return obj.cinema.name

    def get_movie_title(self, obj):
        return obj.movie.title