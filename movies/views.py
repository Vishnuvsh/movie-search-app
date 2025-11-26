from django.shortcuts import render
import requests

# Create your views here.

def movie_search(request):
    movie_data = None
    if request.method == 'POST':
        title = request.POST.get("title")
        api_key = "b545e2e7"
        url = f"http://www.omdbapi.com/?t={title}&apikey={api_key}"
        response = requests.get(url)
        movie_data = response.json()
    return render(request, "search.html", {"movie" : movie_data})