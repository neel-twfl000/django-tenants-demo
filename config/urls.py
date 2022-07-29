from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from base.models import *
from django.contrib.sites.shortcuts import get_current_site

from base.views import *



def add_resort(r):
    site = str(get_current_site(r))
    print(site)
    site = site.replace(":8000", "")
    print(site)
    branch = ResturantBranch.objects.get(sub_domain=site)
    return HttpResponse(f"The Branch Is {branch}")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userList),


    path('branch/', add_resort)
]
