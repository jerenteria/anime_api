from django.shortcuts import render, redirect
# allows to interact with websites
import requests
import json


# URL = "https://api.waifu.pics/type/category"

# def index(request):
#     url_json = requests.get(URL)
#     data = json.loads(url_json.text)
#     print(data)
#     return render(request, "index.html")

URL = "https://api.waifu.pics/type/category"

def get_joke():
    api_end_point = "https://official-joke-api.appspot.com/jokes/random"
    joke = requests.get(api_end_point)
    json_data = json.loads(joke.text)
    print(json_data)

if __name__ == "__main__":
    get_joke()