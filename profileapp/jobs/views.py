from django.shortcuts import render
from django.http import HttpResponse


def winner(request):
    return HttpResponse('<p> Welcome to my page! </p>')
