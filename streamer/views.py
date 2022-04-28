from django.shortcuts import render
import logging
import base64
import sys
import datetime, json
from datetime import datetime, timedelta
from json import JSONEncoder
import json
from decimal import Decimal
from django.utils.dateparse import parse_date

from decimal import Decimal
from django.db.models import Sum
from django.shortcuts import render , redirect
from django.views import View
from streamer.models import videos
from django.http import HttpResponse, JsonResponse
from django.template import Context, Template
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import get_language

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from video_streamer.encoders import DefaultEncoder

# Create your views here.

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)                
                return redirect('index')
            else:
                messages.info(request, "Incorrect Username (Or) Password")
        else:
            messages.info(request, "Invalid Username (Or) Password")

    return render(request , "log.html")


def UserLogout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect("login")


class Home(View):
    template_name = "index.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)


class VideoUpload(View):
    template_name = "video_upload.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)



def uploadVideo(request):
    if request.method == 'POST':
        Title = request.POST.get("title")
        Description = request.POST.get("desc")
        VideoUpload = request.FILES['video']
        ImageUpload = request.FILES['thumbnail']

        
        VideoDB = videos(
            title = Title,
            description = Description,
            video = VideoUpload,
            thumbnail = ImageUpload
        )

        VideoDB.save()

        return redirect("humanbooks")



class books(View):
    template_name = "books.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)

class humanbooks(View):
    template_name = "humanbooks.html"

    @method_decorator(login_required)
    def get(self , request):
        context = {
            'video_data' : json.dumps(list(videos.objects.values()),cls=DefaultEncoder)
        }
        return render(request , self.template_name , context)

class appoinment(View):
    template_name = "appoinment.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)

class contactus(View):
    template_name = "contactus.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)

class log(View):
    template_name = "log.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)

class sign(View):
    template_name = "sign.html"

    @method_decorator(login_required)
    def get(self , request):
        return render(request , self.template_name)

