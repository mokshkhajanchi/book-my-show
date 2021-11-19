import datetime

from rest_framework.test import APITestCase
from core.models import Movie, Cinema, CinemaSeat, Showtime, Reservation


class BaseTestCase(APITestCase):
    def setUp(self):
        movie = {
            'created_at': datetime.datetime(2021, 11, 14, 16, 43, 0, 414042),
            'deleted_at': None,
            'description': 'Venom 2: Let there be Carnage',
            'duration': 120,
            'id': 1,
            'is_deleted': False,
            'release_date': datetime.date(2021, 11, 14),
            'title': 'Venom 2: Let there be Carnage',
            'updated_at': datetime.datetime(2021, 11, 14, 16, 43, 0, 414138)
        }
        obj_movie = Movie(**movie)
        obj_movie.save()

        cinema_1 = {
            'city': 'Mumbai',
            'created_at': datetime.datetime(2021, 11, 14, 16, 50, 23, 104926),
            'deleted_at': None,
            'id': 1,
            'is_deleted': False,
            'name': 'Mumbai Movietime',
            'total_seats': 100,
            'updated_at': datetime.datetime(2021, 11, 14, 19, 52, 21, 916001)
        }
        obj_cinema_1 = Cinema(**cinema_1)
        obj_cinema_1.save()

        cinema_2 = {
            'city': 'Delhi',
            'created_at': datetime.datetime(2021, 11, 14, 16, 50, 37, 927683),
            'deleted_at': None,
            'id': 2,
            'is_deleted': False,
            'name': 'Delhi Movietime',
            'total_seats': 100,
            'updated_at': datetime.datetime(2021, 11, 14, 16, 50, 37, 927737)
        }
        obj_cinema_2 = Cinema(**cinema_2)
        obj_cinema_2.save()

        cinema_3 = {
            'city': 'Hyderabad',
            'created_at': datetime.datetime(2021, 11, 14, 16, 51, 24, 713609),
            'deleted_at': None,
            'id': 3,
            'is_deleted': False,
            'name': 'Hyderabad Movietime',
            'total_seats': 75,
            'updated_at': datetime.datetime(2021, 11, 14, 16, 51, 24, 713671)
        }
        obj_cinema_3 = Cinema(**cinema_3)
        obj_cinema_3.save()

        cinema_4 = {
            'city': 'Chennai',
            'created_at': datetime.datetime(2021, 11, 14, 16, 51, 45, 35029),
            'deleted_at': None,
            'id': 4,
            'is_deleted': False,
            'name': 'Chennai Movietime',
            'total_seats': 80,
            'updated_at': datetime.datetime(2021, 11, 14, 16, 51, 45, 35120)
        }
        obj_cinema_4 = Cinema(**cinema_4)
        obj_cinema_4.save()

        showtime_1 = {
            'cinema_id': 1,
            'created_at': datetime.datetime(2021, 11, 14, 16, 52, 55, 823160),
            'date': datetime.date(2021, 11, 14),
            'deleted_at': None,
            'end_time': datetime.datetime(2021, 11, 14, 20, 0),
            'id': 1,
            'is_deleted': False,
            'movie_id': 1,
            'start_time': datetime.datetime(2021, 11, 14, 18, 0),
            'updated_at': datetime.datetime(2021, 11, 14, 16, 52, 55, 823186)
        }
        obj_showtime_1 = Showtime(**showtime_1)
        obj_showtime_1.save()

        showtime_2 = {
            'cinema_id': 2,
            'created_at': datetime.datetime(2021, 11, 14, 16, 57, 56, 893375),
            'date': datetime.date(2021, 11, 14),
            'deleted_at': None,
            'end_time': datetime.datetime(2021, 11, 14, 20, 0),
            'id': 2,
            'is_deleted': False,
            'movie_id': 1,
            'start_time': datetime.datetime(2021, 11, 14, 18, 0),
            'updated_at': datetime.datetime(2021, 11, 14, 16, 57, 56, 893440)
        }
        obj_showtime_2 = Showtime(**showtime_2)
        obj_showtime_2.save()

        cinema_seat = {
            'available_seats': 61,
            'created_at': datetime.datetime(2021, 11, 16, 20, 10, 26, 661881),
            'deleted_at': None,
            'id': 1,
            'is_deleted': False,
            'showtime_id': 1,
            'updated_at': datetime.datetime(2021, 11, 16, 20, 49, 39, 254729)
        }
        obj_cinema_seat = CinemaSeat(**cinema_seat)
        obj_cinema_seat.save()
        

    def tearDown(self):
        pass