from django.shortcuts import render ,redirect,get_object_or_404
from .forms import PartymenuForm
from .models import Partymenu
from django.contrib.auth.models import User ,auth
from django.contrib.auth import logout
from django.contrib import messages
from bhojan.function import handle_uploaded_file
from bhojan.db import p_menu
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json
import MySQLdb

# Create your views here.

def home(request):
   
    return render(request,'index.html')

def profile(request):

    menu = Partymenu.objects.all()
    paginator = Paginator(menu, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    menu = paginator.get_page(page_number)

    return render(request,'bhojan_profile.html',{'menu':menu})

def weekmenu(request):
    return render(request,'everyweekmenu.html')

def partymenu(request):
    l = {'category':[]}
    k = p_menu(l)
    # print(k)
    context = {
        'menu' :l['category']
    }
    return render(request,'partymenu.html',context)

def contactus(request):
    return render(request,'contact.html')

@login_required(login_url='login')
def partymenuadd(request):  
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == "POST":
            form = PartymenuForm(request.POST , request.FILES)

            if form.is_valid():
                handle_uploaded_file(request.FILES['img'])
                new_obj = form.save(commit=False)
                new_obj.created_by = request.user
                new_obj.save()
                messages.info(request,'New Item added successfully')
                return redirect('pmform')
            else:
                messages.info(request,'invalid data')
                return redirect('pmform')
        
        form = PartymenuForm()
        
        return render(request,'pmform.html',{'form':form })
    else:
        messages.info(request,'OOPS..! You are not a Superuser...')
        return redirect('home')


def register(request):

    if request.method=='POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already exist')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Emaail already exist')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                return redirect('login')
                messages.info(request,'User created successfully')
        else:
            messages.info(request,'Passwords not matching')
    return render(request,'register.html')

def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def dashboard(request):
    if request.user.is_authenticated and request.user.is_superuser:
        # menu = Partymenu.objects.all()
        l = {'category':[]}
        k = p_menu(l)
    
        context ={
        'menu' : l['category'],
        }
        # print(l)
        return render(request,'dashboard.html',context)
    else:
        messages.info(request,'OOPS..! You are not a Superuser...')
        return redirect('home')

@login_required(login_url='login')
def updatemenu(request,id):
    if request.user.is_authenticated and request.user.is_superuser:
        menu = get_object_or_404(Partymenu,id=id)

        if request.method=="POST":
            form = PartymenuForm(request.POST or None,request.FILES or None,    instance=menu)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form =PartymenuForm(instance=menu)
        return render(request,'updatemenu.html',{'form':form ,'menu':menu})
    else:
        messages.info(request,'OOPS..! You are not a Superuser...')
        return redirect('home')

    
@login_required(login_url='login')
def deleteitem(request,id):
    if request.user.is_authenticated and request.user.is_superuser:
        menu = get_object_or_404(Partymenu,id=id)
        menu.delete()
        return redirect('dashboard')
    else:
        messages.info(request,'OOPS..! You are not a Superuser...')
        return redirect('home')
