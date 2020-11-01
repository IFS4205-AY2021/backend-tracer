from django.shortcuts import render
from django.views.decorators import csrf
from django.http import HttpResponse
import pygraphviz as pgv
import collections 
from collections import deque
from .models import UserInfo, Contact, Record
from user.models import *
# from .models import UserInfo, Contact, Record

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def search_status(request):
    if request.POST:
        context = {}
        user = UserInfo.objects.filter(phone=request.POST['phone'])
        if len(user) == 0:
            context['test_result'] = "No such user in the system"
            return render(request, "home.html", context)
        test_result = user[0].test_result
        context['test_result'] = test_result

        user = UserInfo.objects.filter(phone=request.POST['phone'])
        
        contacts1 = Contact.objects.filter(user1=user[0].relate)
        contacts2 = Contact.objects.filter(user2=user[0].relate)
        
        if len(contacts1) == 0 and len(contacts2) == 0:
            context['results'] = "No contact for this person"
            return render(request, "home.html", context)
        
        context['results'] = "Contacts with:"
        context['phone'] = []
        for contact in contacts1:
            user1 = UserInfo.objects.filter(relate=contact.user2)
            context['phone'].append(user1[0].phone)

        for contact in contacts2:
            user2 = UserInfo.objects.filter(relate=contact.user1)
            context['phone'].append(user2[0].phone)
        
        contacts = Contact.objects.all()
        A = pgv.AGraph(directed=True)
        A.node_attr['style']='filled'
        s = set()
        for contact in contacts:
            user1 = UserInfo.objects.filter(relate=contact.user1)
            if user1[0].phone not in s:
                s.add(user1[0].phone)
                A.add_node(user1[0].phone)
                if user1[0].test_result == "True":
                    n = A.get_node(user1[0].phone)
                    n.attr['fillcolor']="#F94848"
                else:
                    n = A.get_node(user1[0].phone)
                    n.attr['fillcolor']="#FFFFFF"
        
            user2 = UserInfo.objects.filter(relate=contact.user2)
            if user2[0].phone not in s:
                s.add(user2[0].phone)
                A.add_node(user2[0].phone)
                if user2[0].test_result == "True":
                    n = A.get_node(user2[0].phone)
                    n.attr['fillcolor']="#F94848"
                else:
                    n = A.get_node(user2[0].phone)
                    n.attr['fillcolor']="#FFFFFF"
        
        sp = set()
        for contact in contacts:
            user1 = UserInfo.objects.filter(relate=contact.user1)
            user2 = UserInfo.objects.filter(relate=contact.user2)
            if (user1[0].phone, user2[0].phone) not in sp:
                sp.add((user1[0].phone, user2[0].phone))
                A.add_edges_from([(user1[0].phone, user2[0].phone)])

        A.layout(prog='dot')
        A.draw(path="media/graph.png", prog='dot')
        context['img'] = "img"
        return render(request, "home.html", context)

    


def change_status(request):
    if request.POST:
        context = {}
        user = UserInfo.objects.get(phone=request.POST['phone'])
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

        user.save()
        context['msg'] = "changed sucessfully"
        return render(request, "home.html", context)

    return HttpResponse("Invalid request")


def search_contact(request):
    if request.POST:
        context = {}
        user1 = UserInfo.objects.filter(phone=request.POST['phone1'])
        user2 = UserInfo.objects.filter(phone=request.POST['phone2'])

        contacts1 = Contact.objects.filter(user1=user1[0].relate)
        contacts2 = Contact.objects.filter(user2=user2[0].relate)
        
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
        user1 = UserInfo.objects.filter(phone=request.POST['phone1'])
        user2 = UserInfo.objects.filter(phone=request.POST['phone2'])
        if  len(user1) > 0 and len(user2) > 0:
            pair = Contact(user1=user1[0].relate, user2=user2[0].relate)
            pair.save()
            context['addmsg'] = "Added sucessfully"
        else:
            context['addmsg'] = "invalid phone number"
        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")

def delete_contact(request):
    if request.POST:
        context = {}
        user1 = UserInfo.objects.filter(phone=request.POST['phone1'])
        user2 = UserInfo.objects.filter(phone=request.POST['phone2'])
        if len(user1) == 0 or len(user2) == 0:
            context['delmsg'] = "No such user in the system"
            return render(request, "home.html", context)
            
        Contact.objects.filter(user1=user1[0].relate, user2=user2[0].relate).delete()
        Contact.objects.filter(user1=user2[0].relate, user2=user1[0].relate).delete()
        context['delmsg'] = "Delete sucessfully"
        return render(request, "home.html", context)

    return HttpResponse("Invalid request")

def search_records(request):
    if request.POST:
        context = {}
        user = UserInfo.objects.filter(phone=request.POST['phone'])
        if len(user) == 0:
            context['recmsg'] = "No such user in the system"
            return render(request, "home.html", context)
    
        records = Record.objects.filter(user=user[0].relate)
        if len(records) == 0:
            context['recmsg'] = "No such record in the system"
            return render(request, "home.html", context)
        
        context['records'] = []
        for record in records:
            context['records'].append(record.time)
            context['records'].append(record.location)
            context['records'].append(record.address)  
            context['records'].append("next")       

        return render(request, "home.html", context)
    
    return HttpResponse("Invalid request")

def generate_graph(request):
    contacts = Contact.objects.all()
    A = pgv.AGraph(directed=True)
    A.node_attr['style']='filled'
    s = set()
    for contact in contacts:
        user1 = UserInfo.objects.filter(relate=contact.user1)
        if user1[0].phone not in s:
            s.add(user1[0].phone)
            A.add_node(user1[0].phone)
            if user1[0].test_result == "True":
                n = A.get_node(user1[0].phone)
                n.attr['fillcolor']="#F94848"
            else:
                n = A.get_node(user1[0].phone)
                n.attr['fillcolor']="#FFFFFF"
        
        user2 = UserInfo.objects.filter(relate=contact.user2)
        if user2[0].phone not in s:
            s.add(user2[0].phone)
            A.add_node(user2[0].phone)
            if user2[0].test_result == "True":
                n = A.get_node(user2[0].phone)
                n.attr['fillcolor']="#F94848"
            else:
                n = A.get_node(user2[0].phone)
                n.attr['fillcolor']="#FFFFFF"
        
    sp = set()
    for contact in contacts:
        user1 = UserInfo.objects.filter(relate=contact.user1)
        user2 = UserInfo.objects.filter(relate=contact.user2)
        if (user1[0].phone, user2[0].phone) not in sp:
            sp.add((user1[0].phone, user2[0].phone))
            A.add_edges_from([(user1[0].phone, user2[0].phone)])

    A.layout(prog='dot')
    A.draw(path="media/graph.png", prog='dot')
    return render(request, "home.html", {}) 

def initiate_cluster(request):
    users = UserInfo.objects.all()
    cluster = 1
    for user in users:
        id = user.relate
        u = UserInfo.objects.get(relate=id)
        if u.test_result == 'True':
            u.cluster_id = cluster
            u.save()
            cluster += 1
        else:
            u.cluster_id = 0
            u.save()

    return render(request, "home.html", {}) 