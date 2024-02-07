from django.shortcuts import render,redirect
from django.http import Http404
from .models import *

# Create your views here.

def User_register (request):
    if request.method == 'POST':
        try:
            User.objects.get(email=request.POST['email'])
            msg = "Email is already register"
            user = User.objects.all()
            return render(request,'index.html',{'msg':msg,'user':user})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password'],
                )
                msg = "user created"
                user = User.objects.all()
                return render(request,'index.html',{'msg':msg,'user':user})
            else:
                msg = "password and confirm password does not match"
                user = User.objects.all()
                return render(request,'index.html',{'msg':msg,'user':user})
    user = User.objects.all()
    return render(request,'index.html',{'user':user})

def user_delete(request,pk):
    try:
        uid = User.objects.get(id=pk)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    print(uid)
    uid.delete()
    return redirect('index')

def user_update(request,pk):
    uid = User.objects.get(id=pk)
    if request.method == "POST":
        uid.name = request.POST['name']
        uid.email = request.POST['email']
        uid.password = request.POST['password']
        uid.save()
        return redirect('index')
    return render(request,'edit.html',{"uid":uid})

def user_search(request):
    if 'name' in request.GET:
        search_name = request.GET['name']
        user = User.objects.filter(name=search_name)
        print(user)
        return render(request,'index.html',{'user':user})
    else:
        msg = "Search query not provided"
        return render(request, 'index.html', {'msg': msg})