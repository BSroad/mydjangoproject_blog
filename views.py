from django.shortcuts import render
from .models import Sitepages


# Create your views here.
def about(request):
    sitepages = Sitepages.objects.all()
    return render(request, 'sitepages/about.html', {'sitepages': sitepages})
