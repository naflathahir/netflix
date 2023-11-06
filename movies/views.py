from django.shortcuts import render
import requests
def index(request):
    import requests

    url = "https://api.themoviedb.org/3/movie/changes?page=1"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0OWQwMTI4ODMyZTQ0MzNhOThlMTZlOGJhNWEzYjgyMiIsInN1YiI6IjY1MzIyNWJlNDgxMzgyMDBlMjg5NjA4NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.b9bMG7X0dU5c__6-ki61WhQQrMl1FHGWM4IMBEDp3Kk"
     }

    response = requests.get(url, headers=headers)

    print(response.text)
 
    #print(response.text)
    posts = response.json()
    data = posts['results']
    return render(request,"index.html",{"data":data})

# Create your views here.
