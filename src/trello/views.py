"""hello world"""

from django.http import HttpResponse, HttpResponseRedirect


def home(request):
    return HttpResponseRedirect("/boards/")


def hello_world(request):
    """hello world"""
    return HttpResponse("Hello, World!")


def qwerty() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5


def qwerty1() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5


def qwerty2() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5


def qwerty3() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5


def qwerty4() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5


def qwerty5() -> int:
    """
    Returns the integer 5.

    Returns:
        int: The number 5.
    """
    return 5
