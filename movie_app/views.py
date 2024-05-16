from django.shortcuts import render
from .api import fetch_movies
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
import matplotlib.pyplot as plt
import io
import urllib
import base64




def top_rated_movies(movies):
    return sorted(movies, key=lambda movie: movie.get('rating', 0), reverse=True)[:10]

def most_recent_movies(movies):
    return sorted(movies, key=lambda movie: movie.get('year', 0), reverse=True)[:10]

def movies_by_genres(movies, genres):
    return [movie for movie in movies if genres.lower() in movie.get('genres', [])]





def generate_report_image(movies):
    # Process data to get movie counts by genre
    genre_counts = {}
    for movie in movies:
        for genre in movie.get('genres', []):
            genre_counts[genre] = genre_counts.get(genre, 0) + 1

    # Create bar chart
    genres = list(genre_counts.keys())
    movie_counts = list(genre_counts.values())
    plt.bar(genres, movie_counts)
    plt.xlabel('Genre')
    plt.ylabel('Number of Movies')
    plt.title('Number of Movies by Genre')

    # Convert the plot to a data URI
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plot_data_uri = "data:image/png;base64," + urllib.parse.quote(base64.b64encode(buffer.getvalue()).decode())

    # Clear the plot
    plt.clf()

    return plot_data_uri

def report(request):
    # Fetch movies data from API
    movies_data = fetch_movies()
    # print("movies_data:", movies_data)  # Add this line for debugging
    if movies_data and 'data' in movies_data:
        movies = movies_data['data'].get('movies', [])
    else:
        movies = []

    # Generate report image
    plot_data_uri = generate_report_image(movies)

    return render(request, 'report.html', {'plot_data_uri': plot_data_uri})



def home(request):
    all_movies = []  # Initialize an empty list to store all movies

    # Fetch all movies from the YTS API until reaching 1000 movies
    page_number = 1
    while len(all_movies) <= 100:
        # Fetch movies for the current page
        movies_data = fetch_movies(limit=20, page=page_number)

        # Check if movies were fetched successfully
        if movies_data and 'data' in movies_data:
            movies = movies_data['data'].get('movies', [])
            all_movies.extend(movies)  # Add fetched movies to the list

        # Increment page number for the next iteration
        page_number += 1

    # Prepare download URLs for each movie
    for movie in all_movies:
        movie['download_720p'] = f"https://example.com/download/{movie['id']}/720p"
        movie['download_1080p'] = f"https://example.com/download/{movie['id']}/1080p"

    # Paginate all movies
    paginator = Paginator(all_movies, 20)  # Show 20 movies per page
    page_number = request.GET.get('page', 1)  # Get the page number from the request, default to 1
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    # Placeholder for additional data processing
    top_rated = sorted(all_movies, key=lambda movie: movie.get('rating', 0), reverse=True)[:10]
    most_recent = sorted(all_movies, key=lambda movie: movie.get('year', 0), reverse=True)[:10]
    genres = ['Action', 'Comedy', 'Drama', 'Horror']  # Example list of genres
    genre_movies = {genre: [movie for movie in all_movies if genre in movie.get('genres', [])] for genre in genres} 
    years = list(range(1999, 2025))

    report_graph_path = None

    return render(request, 'index.html', {
        'movies': page_obj, 
        'top_rated': top_rated, 
        'recent_movies': most_recent, 
        'genre_movies': genre_movies, 
        'genres': genres, 
        'years': years,
        'report_graph_path': report_graph_path
    })







def login(request):
    pass
def register(request):
    pass
def logout(request):
    return render(request, "logout,html")