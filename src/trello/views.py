"""hello world"""

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("/boards/")


def hello_world(request):
    """hello world"""
    return HttpResponse("Hello, World!")


def qwerty():
    return 5


def qwerty1():
    return 5


def qwerty2():
    return 5


def qwerty3():
    return 5


def qwerty4():
    return 5


def qwerty5():
    return 5
