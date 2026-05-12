from django.shortcuts import render
from .models import PageVisit
# Create your views here.

def homePage(request):
    queryset = PageVisit.objects.all()
    home_html = 'home.html'
    context = {"queryset":queryset.count()}
    return render(request, home_html, context)