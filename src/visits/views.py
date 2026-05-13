from django.shortcuts import render
from .models import PageVisit
# Create your views here.

def homePage(request):
    username = request.user.username
    user = username.capitalize()
    queryset = PageVisit.objects.all()
    home_html = 'home.html'
    context = {"querysets":queryset,
               "username":user,
               "list":"Hello Wen"}
    return render(request, home_html, context)