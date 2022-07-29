from django.db import models
from base.models import BaseModel, Account

# Create your models here.


class Resturant(BaseModel):
    name = models.CharField(max_length=30, unique=True)
    account = models.OneToOneField(Account, on_delete=models.SET_NULL, null=True, blank=True)


class ResturantBranch(BaseModel):
    name = models.CharField(max_length=30, unique=True)
