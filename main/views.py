from django.shortcuts import render
from django.views import View


FILMS = [
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


def index(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


class MoviesView(View):

    def get(self, request):
        return render(
            request,
            'main/movies.html',
            {'films': FILMS}
        )


class MovieDetailView(View):

    def get(self, request, movie_id):

        movie = next(
            (film for film in FILMS if film['id'] == movie_id),
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


class BookingView(View):

    def get(self, request, movie_id):

        movie = next(
            (film for film in FILMS if film['id'] == movie_id),
            None
        )

        if movie is None:
            return render(
                request,
                'main/movie_not_found.html'
            )

        return render(
            request,
            'main/booking.html',
            {'movie': movie}
        )

    def post(self, request, movie_id):

        movie = next(
            (film for film in FILMS if film['id'] == movie_id),
            None
        )

        if movie is None:
            return render(
                request,
                'main/movie_not_found.html'
            )

        name = request.POST.get('name', '').strip()
        tickets = request.POST.get('tickets', '').strip()

        if not name:
            return render(
                request,
                'main/booking.html',
                {
                    'movie': movie,
                    'error': 'Name cannot be empty.'
                }
            )

        try:
            tickets = int(tickets)
        except ValueError:
            tickets = 0

        if tickets <= 0:
            return render(
                request,
                'main/booking.html',
                {
                    'movie': movie,
                    'error': 'Number of tickets must be greater than zero.'
                }
            )

        if movie['seats'] == 0:
            return render(
                request,
                'main/booking.html',
                {
                    'movie': movie,
                    'error': 'This movie is SOLD OUT.'
                }
            )

        if tickets > movie['seats']:
            return render(
                request,
                'main/booking.html',
                {
                    'movie': movie,
                    'error': 'Not enough available seats.'
                }
            )

        movie['seats'] -= tickets

        return render(
            request,
            'main/booking.html',
            {
                'movie': movie,
                'success': True,
                'name': name,
                'tickets': tickets
            }
        )