from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
# Create your views here.


def homepage(request):
    return render(request,"igprofile/homepage.html")

@login_required(login_url='/accounts/login/')    
def reels(request):
    return render (request,"igprofile/reels.html")

@permission_required('igprofile.view_username',login_url='/accounts/login')
def username(request):
    return render(request,"igprofile/username.html")    