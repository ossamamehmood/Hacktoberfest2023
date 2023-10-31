from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    
    if request.method=="POST":
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if User.objects.filter(username=username):
            messages.error(request,"Username already exist! Please try some other username")
            return redirect('home')
            
        if User.objects.filter(email=email):
            pass
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname 
        
        myuser.save()
        messages.success(request,"Your account has been successfully created.")
        
    return render(request,'signup.html')

def signin(request):
    
    if request.method=="POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'index.html',{'fname' : fname})
        else:
            messages.eroor(request,"BAD CREDITANTIALS")
            return redirect('home')
                
    return render(request,'signin.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')

