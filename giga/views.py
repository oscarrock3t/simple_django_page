from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return HttpResponse(request.get_host() + ' is host! GIGA!')
# Create your views here.
