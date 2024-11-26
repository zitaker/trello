"""The boards page"""

import logging

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

logger = logging.getLogger(__name__)


def redirect_to_boards(request: HttpRequest) -> HttpResponseRedirect:
    """Redirects the user to the boards page.

    This function temporarily handles redirection to the `/boards/` endpoint.
    In the future, this functionality may no longer be required.

    Args:
        request (HttpRequest): The incoming HTTP request object.

    Returns:
        HttpResponseRedirect: A redirect response to the `/boards/` page.
    """
    logger.info("Redirecting request from %s to /boards/", request.path)
    return HttpResponseRedirect("/boards/")


def create_board(request: HttpRequest) -> HttpResponse:
    """
    Handles the process of creating a new board. If the 'Create' button is
    clicked, it will show the input field for entering the board title. If
    the board title is provided, it displays a success message. If the
    title is empty, an error message is shown.

    Args:
        request (HttpRequest): The HTTP request object that contains the
                               method and form data.

    Returns:
        HttpResponse: Renders the 'boards.html' template with the appropriate
                      context, either showing the title input field or a
                      message after form submission.
    """
    # The show_input variable controls whether to show the board title
    # entry field
    show_input = False

    # Check if the "Create" button has been clicked
    if request.method == "POST" and "show_input" in request.POST:
        show_input = True

    # The form of creating a board
    if request.method == "POST" and "board_title" in request.POST:
        board_title = request.POST.get("board_title", "").strip()
        if board_title:
            message = f"Transition to the board - '{board_title}'"
        else:
            message = (
                "The board creation button is not"
                " active until there is no name!"
            )
        return render(
            request,
            "boards.html",
            {"message": message, "show_input": show_input},
        )

    return render(request, "boards.html", {"show_input": show_input})
