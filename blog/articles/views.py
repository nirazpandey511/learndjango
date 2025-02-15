

# Create your views here.
# myapp/views.py
from django.shortcuts import render

def welcome(request):
    return render(request, 'articles/welcome.html')
