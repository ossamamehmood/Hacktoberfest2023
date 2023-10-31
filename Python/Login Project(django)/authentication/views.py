from django.http import HttpResponse
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        
        messages.success(request,'Your Account has been successfully created')
        return redirect('signin')
    
    return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        pass1=request.POST['pass1']
        
        user = authenticate(username=username,password=pass1)
        
        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'index.html',{'fname':fname})
        else:
            messages.error(request,"Bad Credentials")
            return redirect('index')
    return render(request,'signin.html')

def signout(request):
    # return render(request,'signout.html')
    pass

