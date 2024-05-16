import requests

def fetch_movies(page=1, limit=10):
    url = f'https://yts.mx/api/v2/list_movies.json?page={page}&limit={limit}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # Handle error response
        return None

