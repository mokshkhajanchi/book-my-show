from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    duration = models.IntegerField(blank=False, null=False)
    release_date = models.DateField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'movie'

CITY_CHOICES = (
    ('Mumbai', 'Mumbai'),
    ('Delhi', 'Delhi'),
    ('Hyderabad', 'Hyderabad'),
    ('Chennai', 'Chennai'),
)

class Cinema(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    total_seats = models.IntegerField(blank=False, null=False)
    city = models.TextField(choices=CITY_CHOICES, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cinema'

class Showtime(models.Model):
    date = models.DateField(blank=False, null=False)
    start_time = models.DateTimeField(blank=False, null=False)
    end_time = models.DateTimeField(blank=False, null=False)
    movie = models.ForeignKey(Movie, on_delete=DO_NOTHING)
    cinema = models.ForeignKey(Cinema, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'showtime'

class CinemaSeat(models.Model):
    available_seats = models.IntegerField(blank=False, null=False)
    showtime = models.ForeignKey(Showtime, on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cinema_seat'

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=DO_NOTHING)
    showtime = models.ForeignKey(Showtime, on_delete=DO_NOTHING)
    number_of_seats = models.IntegerField(blank=False, null=False)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'reservation'