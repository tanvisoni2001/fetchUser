from django.shortcuts import render
import requests
from .models import fetchUser

# Create your views here.

MAIGRET_API_URL =  "https://api.github.com/users/{}"
DAPROFILER_API_URL =  "https://api.github.com/search/users?q={}+in:fullname"
YESITSME_API_URL = "https://api.github.com/search/users?q={}+in:fullname,email,phone"

def fetch_data(API_endpoints, query):
    url = API_endpoints.format(query)
    print(url) 
    response = requests.get(url) 
    if response.status_code == 200:
        return response.json()
    
    return None

def index(request):
    if request.method == "POST":
        username = request.POST['username']
        full_name = request.POST['firstname'] + request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone_no']
      

        maigret_data = fetch_data(MAIGRET_API_URL, username)
        daprofiler_data = fetch_data(DAPROFILER_API_URL, full_name)
        yesitsme_data = fetch_data(YESITSME_API_URL, f"{full_name}+{email}+{phone}")
        
       
        data = {'maigret_data': maigret_data, 'daprofiler_data': daprofiler_data, 'yesitsme_data': yesitsme_data}

        return render(request,'fetchUser/index.html', data)
    return render(request, 'fetchUser/index.html') 



