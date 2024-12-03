"""The boards page"""

import logging

from typing import Optional

from django.views import View
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


class CreateBoardView(View):
    """Handles board-related operations."""

    template_name = "boards.html"

    def get_context_data(
        self, show_input: bool = False, message: Optional[str] = None
    ) -> dict:
        """
        Constructs the context for rendering the template.

        Args:
            show_input (bool): Whether to show the input field.
            message (str): The message to display on the page.

        Returns:
            dict: The context dictionary for the template.
        """
        return {"show_input": show_input, "message": message}

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handles GET requests to render the board creation page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: A response rendering the 'boards.html' template
                          with default context.
        """
        return render(request, self.template_name, self.get_context_data())

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handles POST requests to create a new board.

        Depending on the submitted data, this method toggles the display
        of the input field or validates the board title.

        Args:
            request (HttpRequest): The HTTP request object containing
                                   POST data.

        Returns:
            HttpResponse: A response rendering the 'boards.html' template
                          with context that includes the input field state
                          and any relevant messages.
        """
        if "show_input" in request.POST:
            context = self.get_context_data(show_input=True)
        elif "board_title" in request.POST:
            board_title = request.POST.get("board_title", "").strip()
            if board_title:
                message = f"Transition to the board - '{board_title}'"
            else:
                message = (
                    "The board creation button is not active until "
                    "there is no name!"
                )
            context = self.get_context_data(show_input=False, message=message)
        else:
            context = self.get_context_data()

        return render(request, self.template_name, context)
