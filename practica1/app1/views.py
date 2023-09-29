from django.shortcuts import render

def home(request):
    contex = {}
    return render(request, 'app1/home.html')
