"""
Test the views related to board creation and redirects in the Trello-like app.

This module contains tests for the following views:
- Redirect to boards: tests that accessing the home page redirects to the
  '/boards/' page.
- Create board: tests the creation of a new board with a title, including
  the validation of the title and handling of empty titles.

Each test case verifies the expected behavior and page content, ensuring that
the views work as expected under different scenarios
(e.g., redirect, valid/invalid board title).
"""

import html

import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestRedirectToBoards:
    """Test the redirect_to_boards view."""

    @pytest.fixture
    def client(self) -> Client:
        """Create a client instance to make requests."""
        return Client()

    def test_redirect_to_boards(self, client: Client) -> None:
        """Test that accessing the home page redirects to /boards/."""
        url = reverse("redirect_to_boards")  # URL for the home page
        response = client.get(url)

        # Check that the response is a redirect (status 302)
        assert response.status_code == 302

        # Check that the redirect target is the /boards/ page
        assert response["Location"] == reverse("create_board")


@pytest.mark.django_db
class TestCreateBoard:
    """Test the create_board view."""

    @pytest.fixture
    def client(self) -> Client:
        """Create a client instance to make requests."""
        return Client()

    def test_initial_page_load(self, client: Client) -> None:
        """Test that the page loads initially without the board title input."""
        url = reverse("create_board")
        response = client.get(url)

        # Check that the response status is 200 OK
        assert response.status_code == 200

        # Check that 'show_input' is in the context and its value is False
        assert response.context["show_input"] is False

    def test_show_input_on_create_button_click(self, client: Client) -> None:
        """
        Test that clicking 'Create'
        shows the input field for the board title.
        """
        url = reverse("create_board")

        # Simulate clicking the 'Create' button
        response = client.post(url, {"show_input": "true"})

        # Check that the input field is displayed after clicking 'Create'
        assert response.status_code == 200
        assert response.context["show_input"] is True

    def test_create_board_with_title(self, client: Client) -> None:
        """Test the creation of a board with a title."""
        url = reverse("create_board")

        # Simulate a POST request with the board title
        response = client.post(url, {"board_title": "My Board"})

        # Check that the response status is 200 OK
        assert response.status_code == 200

        # Decode the response content to handle HTML entities
        response_content = response.content.decode()

        # Check if the message is present, with HTML entities decoded
        expected_message = "Transition to the board - 'My Board'"
        assert expected_message in html.unescape(response_content)

    def test_create_board_with_empty_title(self, client: Client) -> None:
        """Test that an error message is shown if the title is empty."""
        url = reverse("create_board")

        # Simulate creating a board with an empty title
        response = client.post(url, {"show_input": "true", "board_title": ""})

        # Check that the error message is displayed
        assert response.status_code == 200
        assert (
            "The board creation button is not active until there is no "
            "name!" in response.content.decode()
        )
