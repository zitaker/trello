"""hello world"""

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("/boards/")


def hello_world(request):
    """hello world"""
    return HttpResponse("Hello, World!")
