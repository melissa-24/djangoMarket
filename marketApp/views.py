from django.shortcuts import render, HttpResponse, redirect

CATEGORY = {
    'Food',
    'Crafts'
}

def index(request):
    return render(request, "index.html")




