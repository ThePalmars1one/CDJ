from django.shortcuts import render
from .models import Consejos

def home(request):
    consejos = Consejos.objects.all()
    return render(request, 'home.html', {'Consejos': consejos})
