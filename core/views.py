import logging
import pprint

from django.shortcuts import render
from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from .models import Cinema, CinemaSeat, Showtime, Reservation

logger = logging.getLogger('django_core')

class MovieView(viewsets.ViewSet):
    def get_movies_as_per_city(self, request):
        try:
            result = {
                'message': 'Movies retrieved successfully',
                'status': True,
                'data': []
            }

            if not request.data:
                result['message'] = 'Request body is empty'
                result['status'] = False
                return Response(result, status=status.HTTP_200_OK)

            city = request.data.get('city', '')
            shows = Showtime.objects.filter(is_deleted=0)
            for show in shows:
                if show.cinema.city == city:
                    record = {
                        'show_id': show.id,
                        'movie_id': show.movie.id,
                        'city': show.cinema.city,
                        'movie': show.movie.title,
                        'description': show.movie.description,
                        'duration': show.movie.duration,
                        'date': show.date,
                        'from': show.start_time,
                        'to': show.end_time
                    }  
                    result['data'].append(record)           

            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            error_result = {
                'message': str(e),
                'status': False,
                'data': []
            }

            logger.error('Error in MovieView get_movies_as_per_city')
            logger.error('Exception: {0}'.format(str(e)))

            return Response(error_result, status=status.HTTP_400_BAD_REQUEST)

    def get_cinemas_as_per_movie(self, request):
        try:
            result = {
                'message': 'Cinemas retrieved successfully',
                'status': True,
                'data': []
            }

            if not request.data:
                result['message'] = 'Request body is empty'
                result['status'] = False
                return Response(result, status=status.HTTP_200_OK)

            movie = request.data.get('movie', '')
            shows = Showtime.objects.filter(is_deleted=0)
            for show in shows:
                if show.movie.title == movie:
                    record = {
                        'id': show.id,
                        'cinema_id': show.cinema.id,
                        'city': show.cinema.city,
                        'movie': show.movie.title,
                        'description': show.movie.description,
                        'duration': show.movie.duration,
                        'date': show.date,
                        'from': show.start_time,
                        'to': show.end_time
                    }  
                    result['data'].append(record)           

            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            error_result = {
                'message': str(e),
                'status': False,
                'data': []
            }

            logger.error('Error in MovieView get_cinemas_as_per_movie')
            logger.error('Exception: {0}'.format(str(e)))

            return Response(error_result, status=status.HTTP_400_BAD_REQUEST)

    def get_seats_as_per_showtime(self, request):
        try:
            result = {
                'message': 'Seats retrieved successfully',
                'status': True,
                'data': []
            }

            if not request.data:
                result['message'] = 'Request body is empty'
                result['status'] = False
                return Response(result, status=status.HTTP_200_OK)

            showtime_id = request.data.get('showtime_id', '')
            cinema_seats = CinemaSeat.objects.filter(is_deleted=0, showtime=showtime_id)
            for cinema_seat in cinema_seats:
                record = {
                    'id': cinema_seat.id,
                    'available_seats': cinema_seat.available_seats,
                    'cinema_id': cinema_seat.showtime.cinema.id,
                    'city': cinema_seat.showtime.cinema.city,
                    'movie': cinema_seat.showtime.movie.title,
                    'description': cinema_seat.showtime.movie.description,
                    'duration': cinema_seat.showtime.movie.duration,
                    'date': cinema_seat.showtime.date,
                    'from': cinema_seat.showtime.start_time,
                    'to': cinema_seat.showtime.end_time
                }  
                result['data'].append(record)           

            return Response(result, status=status.HTTP_200_OK)
        except Exception as e:
            error_result = {
                'message': str(e),
                'status': False,
                'data': []
            }

            logger.error('Error in MovieView get_seats_as_per_showtime')
            logger.error('Exception: {0}'.format(str(e)))

            return Response(error_result, status=status.HTTP_400_BAD_REQUEST)

class ReservationView(viewsets.ViewSet):
    permission_classes = (permissions.IsAuthenticated,)

    def reserve_tickets(self, request):
        try:
            result = {
                'message': 'Seats reserved successfully',
                'status': True,
                'data': []
            }

            if not request.data:
                result['message'] = 'Request body is empty'
                result['status'] = False
                return Response(result, status=status.HTTP_200_OK)

            showtime_id = request.data.get('showtime_id', '')
            number_of_seats = request.data.get('number_of_seats', 0)

            cinema_seat = CinemaSeat.objects.get(is_deleted=0, showtime_id=showtime_id)
            if cinema_seat.available_seats < number_of_seats:
                result['message'] = 'Seats are not available'
                result['status'] = True
                record = {
                    'id': cinema_seat.id,
                    'available_seats': cinema_seat.available_seats,
                    'cinema_id': cinema_seat.showtime.cinema.id,
                    'city': cinema_seat.showtime.cinema.city,
                    'movie': cinema_seat.showtime.movie.title,
                    'description': cinema_seat.showtime.movie.description,
                    'duration': cinema_seat.showtime.movie.duration,
                    'date': cinema_seat.showtime.date,
                    'from': cinema_seat.showtime.start_time,
                    'to': cinema_seat.showtime.end_time
                }
                result['data'].append(record)
                return Response(result, status=status.HTTP_200_OK)


            obj = Reservation(
                user = request.user,
                showtime = cinema_seat.showtime,
                number_of_seats = number_of_seats,
                status = True,
                is_deleted = 0,
                deleted_at = None
            )
            obj.save()
            cinema_seat.available_seats = cinema_seat.available_seats - number_of_seats
            cinema_seat.save()

            result['message'] = 'Ticket is reserved successfully'
            del obj._state
            result['data'].append(obj.__dict__)
            return Response(result, status=status.HTTP_200_OK)


        except Exception as e:
            error_result = {
                'message': str(e),
                'status': False,
                'data': []
            }

            logger.error('Error in ReservationView reserve_tickets')
            logger.error('Exception: {0}'.format(str(e)))

            return Response(error_result, status=status.HTTP_400_BAD_REQUEST)
        