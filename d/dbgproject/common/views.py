from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .models import * 
from dbg.models import *
from django.contrib import auth

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data = request.POST)
        if form.is_valid():
            user_id = request.POST["user_id"]
            user_password= request.POST["user_password"]
            user = authenticate(request=request,user_id=user_id, user_password=user_password)
            if user is not None:
                login(request, user)
        return redirect("home")

    else:
        form=AuthenticationForm()
        return render(request, "login.html")
         


def logout_view(request):
    logout(request)
    return redirect("home")

def signUp(request):
     if request.method == 'POST':
         if request.POST['password1']== request.POST['password2']:
            user = User.objects.create_user(
                user_name=request.POST['name'],                #실명
                user_nickname=request.POST['nickname'],        #닉네임
                username=request.POST['id'],                   #이메일
                password=request.POST['password1'],            #비밀번호
                user_phone_number=request.POST['phone_number'],   #전화번호
                user_link_facebook=request.POST['link_linkaccount1'],        #페이스북계정
                user_link_twitter=request.POST['link_linkaccount2'],         #트위터 계정
                user_link_instagram=request.POST['link_linkaccount3'],        #인스타그램 계정
            )
            auth.login(request, user)
            return redirect("home")
            
     else:
         form: UserCreationForm
         return render(request, "signUp.html")
    
