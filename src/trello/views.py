"""hello world"""

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("/boards/")


def hello_world(request):
    """hello world"""
    return HttpResponse("Hello, World!")


def qwerty() -> int:
    return 5


def qwerty1() -> int:
    return 5


def qwerty2() -> int:
    return 5


def qwerty3() -> str:
    return 5


def qwerty4() -> int:
    return 5


def qwerty5() -> int:
    return 5
