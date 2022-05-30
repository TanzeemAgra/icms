from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import fields
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
from django.core.paginator import Paginator
from django.forms import ModelForm, Textarea
#from django.utils.translation import ugettext_lazy as _
from django.shortcuts import redirect
from django import forms

# Create your views here.

def index(request):
    return render(request, 'index.html')

