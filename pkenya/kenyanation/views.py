from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from pkenya.authentication.models import Profile
from . models import PolicalPatie

def nationlist(request):
    list_patis=PolicalPatie.objects.order_by('-year')
    return render(request,"kenyanation/list.html",{"natinal_list":list_patis})
