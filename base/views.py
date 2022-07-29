from django.http import HttpResponse
from django.shortcuts import render
from . models import *
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def get_branch(request):
    sub_domain = str(get_current_site(request))
    branch = ResturantBranch.objects.get(sub_domain=sub_domain)
    return branch

def userList(request):
    user_list = Account.objects.all()
    print(user_list)
    return HttpResponse("OK")


