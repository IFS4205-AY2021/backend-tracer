from django.shortcuts import render
from django.views.decorators import csrf
from .models import User

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def search_status(request):
    if request.POST:
        user = User.objects.get(id = request['id'])
        test_result = user.test_result
        return render(request, 'home.html', {"test_result": test_result})
    
    return render(request, 'home.html', "Invalid request")


def change_status(request):
    if request.POST:
        user = User.objects.get(id = request['id'])
        user.test_result = request['status']
        user.save()
        return render(request, 'home.html', {"change": "Successful"})

    return render(request, 'home.html', "Invalid request")

def delete_people(request):
    if request.POST:
        user = User.objects.get(id = request['id'])
        user.delete()
        return render(request, 'home.html', {"delete": "Successful"})
    
    return render(request, 'home.html', "Invalid request")
