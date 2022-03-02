from django.shortcuts import render, redirect
# allows to interact with websites
import requests
import json



def index(request):
    response = requests.get("http://api.open-notify.org/astros.json")
    query = {'lat':'45', 'lon':'180'}
    response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    print(response.json())
    context = {
        'data': query,
    }
    return render(request, "index.html", context)



