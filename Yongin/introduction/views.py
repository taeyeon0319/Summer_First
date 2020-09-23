from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'introduction/home.html')

def activity(request):
    return render(request, 'introduction/activity.html')

def delicious(request) :
    return render(request, 'introduction/delicious.html')

def photo(request) :
    return render(request, 'introduction/photo.html')