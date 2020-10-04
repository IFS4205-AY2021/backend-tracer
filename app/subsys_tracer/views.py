from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
from .models import User, Contact, Record

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def search_status(request):
    if request.POST:
        context = {}
        user = User.objects.filter(phone=request.POST['phone'])
        if len(user) == 0:
            context['test_result'] = "No such user in the system"
            return render(request, "home.html", context)
        test_result = user[0].test_result
        context['test_result'] = test_result
        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")


def change_status(request):
    if request.POST:
        context = {}
        user = User.objects.get(phone=request.POST['phone'])
        test_result = request.POST['status']
        if test_result != "positive" and test_result != "negative" and test_result != "unknown":
            context['msg'] = "invalid status"
            return render(request, "home.html", context)
        elif test_result == "positive":
            user.test_result = True
        elif test_result == "negative":
            user.test_result = False
        else:
            user.test_result = None

        user.age = 33
        user.save()
        context['msg'] = "changed sucessfully"
        return render(request, "home.html", context)

    return HttpResponse("Invalid request")


def search_contact(request):
    if request.POST:
        context = {}
        contacts1 = Contact.objects.filter(phone1=request.POST['phone'])
        contacts2 = Contact.objects.filter(phone2=request.POST['phone'])
        
        if len(contacts1) == 0 and len(contacts2) == 0:
            context['results'] = "No contact for this person"
            return render(request, "home.html", context)
        
        context['phone'] = []
        for phone in contacts1:
            context['phone'].append(phone.phone2)

        for phone in contacts2:
            context['phone'].append(phone.phone1)

        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")

def add_contact(request):
    if request.POST:
        context = {}
        pair = Contact(phone1=request.POST['phone1'], phone2=request.POST['phone2'])
        pair.save()
        context['addmsg'] = "Added sucessfully"
        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")

def delete_contact(request):
    if request.POST:
        context = {}
        Contact.objects.filter(phone1=request.POST['phone1'], phone2=request.POST['phone2']).delete()
        Contact.objects.filter(phone1=request.POST['phone2'], phone2=request.POST['phone1']).delete()
        context['delmsg'] = "Delete sucessfully"
        return render(request, "home.html", context)

    return HttpResponse("Invalid request")

def search_records(request):
    if request.POST:
        context = {}
        records = Record.objects.filter(phone=request.POST['phone'])
        if len(records) == 0:
            context['recmsg'] = "No such record in the system"
            return render(request, "home.html", context)
        
        context['records'] = []
        for record in records:
            context['records'].append(record.date)
            context['records'].append(record.time)
            context['records'].append(record.location)
            context['records'].append(record.address)  
            context['records'].append("next")       

        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")