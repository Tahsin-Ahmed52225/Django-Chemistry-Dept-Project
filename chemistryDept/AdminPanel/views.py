from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Userinfo,banner
import json

from django.contrib.auth.models import User

#login page viewer
def login_page(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request,'AdminPanel/login.html')

#User login authenticator
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('dashboard'))

            else:
                messages.warning(request, 'Account not active !')
                return HttpResponseRedirect(reverse('login_page'))
        else:
            messages.warning(request, 'Wrong credentials !')
            return HttpResponseRedirect(reverse('login_page'))
    else:
        return HttpResponseRedirect(reverse('login_page'))

#user logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_page'))

#Admin dashboard handler
def dashboard(request):
    if request.user.is_authenticated:
        user = User.objects.get(pk=request.user.id)
        try:
            user_info = Userinfo.objects.get(user__pk= user.id)
        except Userinfo.DoesNotExist:
            user_info = None

        return render(request,"AdminPanel/index.html",context={'user':user, 'user_info':user_info})
    else:
        return HttpResponseRedirect(reverse('login_page'))

#Admin settings
@login_required
def settings(request):
    return render(request,"AdminPanel/settings/index.html")
@login_required
def homebanner(request):
    all_banner = banner.objects.all()
    return render(request,"AdminPanel/settings/homebanner.html",context={'all_banner':all_banner})

#adding home banner
@login_required
def addHomeBanner(request):
    if request.method == "POST":
       new_banner = banner()
       new_banner.banner_title = request.POST.get('banner_title')
       new_banner.banner_subtitle = request.POST.get('banner_subtitle')
       new_banner.banner_description = request.POST.get('banner_description')
       new_banner.banner_url = request.POST.get('banner_url')
       new_banner.banner_cover = request.FILES["banner_cover"]
       new_banner.save()

       messages.success(request, 'New banner added!')
       return HttpResponseRedirect(reverse('homebanner'))
#Delete home banners
@login_required
def deleteHomeBanner(request,id):
    if request.method == "POST":
        banner.objects.filter(id=id).delete()
        messages.success(request, 'Banner Deleted!')
        return HttpResponseRedirect(reverse('homebanner'))
    else:
        return HttpResponseRedirect(reverse('index'))
#Get home banner data
@login_required
def getHomeBanner(request,id):
    banners = banner.objects.get(id=id)
    data = json.dumps(banners.banner_info())
    return JsonResponse({'data': data})

#Edit home banner data
@login_required
def editHomeBanner(request,id):
    if request.method == "POST":
       banners = banner.objects.get(id=id)
       banners.banner_title = request.POST.get('banner_title_edit')
       banners.banner_subtitle = request.POST.get('banner_subtitle_edit')
       banners.banner_description = request.POST.get('banner_description_edit')
       banners.banner_url = request.POST.get('banner_url_edit')
       if bool(request.FILES.get('banner_cover_edit', False)) == True:
         banners.banner_cover = request.FILES["banner_cover_edit"]
       banners.save()
       messages.success(request, 'Banner data changed!')
       return HttpResponseRedirect(reverse('homebanner'))
    else:
       return HttpResponseRedirect(reverse('index'))
