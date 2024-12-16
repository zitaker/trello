"""The boards page"""

import logging

from typing import Optional

from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect

from trello.models import Board

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
        boards = Board.objects.all()
        return {"show_input": show_input, "message": message, "boards": boards}

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

        Args:
            request (HttpRequest): The HTTP request object containing
                                   POST data.

        Returns:
            HttpResponse: A response rendering the 'boards.html' template
                          or redirecting to a newly created board's page.
        """
        if "show_input" in request.POST:
            # Show the form
            context = self.get_context_data(show_input=True)
            return render(request, self.template_name, context)

        if "board_title" in request.POST:
            # Creating a new board
            board_title = request.POST.get("board_title", "").strip()
            if board_title:
                # Creating a Board object and redirecting it to the board page
                board, created = Board.objects.get_or_create(title=board_title)
                if created:
                    return redirect(
                        reverse(
                            "board_detail", kwargs={"board_title": board.title}
                        )
                    )
                # If the board already exists, we display a message
                message = f"A board named '{board_title}' already exists!"
            else:
                message = "The name of the board cannot be empty!"

            # We return the page with the error message
            context = self.get_context_data(show_input=True, message=message)
            return render(request, self.template_name, context)

        return render(request, self.template_name, self.get_context_data())


class BoardDetailView(View):
    """Handles the display of a specific board."""

    template_name = "board_detail.html"

    def get(self, request: HttpRequest, board_title: str) -> HttpResponse:
        """
        Handles GET requests to display a specific board.

        Args:
            request (HttpRequest): The HTTP request object.
            board_title (str): The title of the board to display.

        Returns:
            HttpResponse: A response rendering the 'board_detail.html' template.
        """
        board = get_object_or_404(Board, title=board_title)
        return render(request, self.template_name, {"board": board})
