from django.shortcuts import render

from . import list_themes
from . templatetags import themes

def themes(request):
    return render(request,"themes/themes.html",{'themes':list_themes})
