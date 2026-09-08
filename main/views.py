from django.shortcuts import render
from django.views import View


def index(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')

class BookingView(View):
    def get(self, request, movie_id):
        return render(request, 'main/booking.html')



class MoviesView(View):

    def get(self, request):
        films = [
            {
                'id': 1,
                'title': 'Inception',
                'genre': 'Sci-Fi',
                'duration': 148,
                'age_rating': 16,
                'seats': 10,
            },
            {
                'id': 2,
                'title': 'Interstellar',
                'genre': 'Sci-Fi',
                'duration': 169,
                'age_rating': 12,
                'seats': 0,
            },
            {
                'id': 3,
                'title': 'The Dark Knight',
                'genre': 'Action',
                'duration': 152,
                'age_rating': 16,
                'seats': 5,
            },
            {
                'id': 4,
                'title': 'Titanic',
                'genre': 'Drama',
                'duration': 195,
                'age_rating': 12,
                'seats': 8,
            },
            {
                'id': 5,
                'title': 'Avatar',
                'genre': 'Fantasy',
                'duration': 162,
                'age_rating': 12,
                'seats': 3,
            },
            {
                'id': 6,
                'title': 'The Matrix',
                'genre': 'Action',
                'duration': 136,
                'age_rating': 16,
                'seats': 0,
            },
        ]

        return render(
            request,
            'main/movies.html',
            {'films': films}
        )


class MovieDetailView(View):

    def get(self, request, movie_id):
        films = [
            {
                'id': 1,
                'title': 'Inception',
                'genre': 'Sci-Fi',
                'duration': 148,
                'age_rating': 16,
                'seats': 10,
            },
            {
                'id': 2,
                'title': 'Interstellar',
                'genre': 'Sci-Fi',
                'duration': 169,
                'age_rating': 12,
                'seats': 0,
            },
            {
                'id': 3,
                'title': 'The Dark Knight',
                'genre': 'Action',
                'duration': 152,
                'age_rating': 16,
                'seats': 5,
            },
            {
                'id': 4,
                'title': 'Titanic',
                'genre': 'Drama',
                'duration': 195,
                'age_rating': 12,
                'seats': 8,
            },
            {
                'id': 5,
                'title': 'Avatar',
                'genre': 'Fantasy',
                'duration': 162,
                'age_rating': 12,
                'seats': 3,
            },
            {
                'id': 6,
                'title': 'The Matrix',
                'genre': 'Action',
                'duration': 136,
                'age_rating': 16,
                'seats': 0,
            },
        ]

        movie = next(
            (film for film in films if film['id'] == movie_id),
            None
        )

        if movie is None:
            return render(
                request,
                'main/movie_not_found.html'
            )

        return render(
            request,
            'main/movie.html',
            {'movie': movie}
        )