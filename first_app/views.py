from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, "first_app/index.html")