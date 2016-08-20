from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from pkenya.authentication.models import Profile
from . models import Regions
def regions(request):
    regions=Regions.objects.all()
    return render(request,"diplomats/regions.html",{"regions":regions})

def viewdiplomats(request,region):
    diplomats= Profile.objects.filter(location=region).filter(is_diplomat=True)
    return render(request,"diplomats/diplomats.html",{
                            "diplomats":diplomats,
                            "region":region
    })
