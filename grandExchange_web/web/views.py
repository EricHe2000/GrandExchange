from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    #Ride.objects.all().filter(rideEndLoc=None).delete()
    template_name = 'home.html'