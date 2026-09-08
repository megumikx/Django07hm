from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('movies/', views.MoviesView.as_view(), name='movies' ),
    path('movies/<int:movie_id>/', views.MovieDetailView.as_view(), name='movie'),
    path('bookings/<int:movie_id>/', views.BookingView.as_view(), name='booking'),
]
