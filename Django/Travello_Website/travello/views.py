from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):   
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700

    return render(request, "index.html", {'dest1': dest1})
