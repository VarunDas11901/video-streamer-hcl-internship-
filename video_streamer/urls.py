"""video_streamer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from streamer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view() , name = "index"),
    path('login/', views.UserLogin, name='login'),
    path('logout/' , views.UserLogout , name="logout"),  
    path('video/',views.VideoUpload.as_view() , name = "video"),
    path('upload_video/',views.uploadVideo , name = "upload_video"),
    path('books/',views.books.as_view() , name = "books"),
    path('humanbooks/',views.humanbooks.as_view() , name = "humanbooks"),
    path('appoinment/',views.appoinment.as_view() , name = "appoinment"),
    path('contactus/',views.contactus.as_view() , name = "contactus"),
    path('log/',views.log.as_view() , name = "log"),
    path('sign/',views.sign.as_view() , name = "sign"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

