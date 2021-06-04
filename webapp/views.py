from django.shortcuts import render
from .models import Account
from django.http import HttpResponse

# Create your views here.

from django.http import HttpResponse


def account(request):
    accounts = Account.objects.all()
    return render(request, 'webapp/index.html', {'accounts': accounts})


def details(request, pk):
    user = Account.objects.get(pk=pk)
    return render(request, 'webapp/details.html', {'user': user})


