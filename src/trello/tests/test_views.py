"""
Test the views related to board creation and redirects in the Trello app.

This module contains tests for the following views:
- Redirect to boards: tests that accessing the home page redirects to the
  '/boards/' page.
- Create board: tests the creation of a new board with a title, including
  validation of the title and handling of empty titles.

Each test case verifies expected behavior and page content, ensuring that
the views function correctly under various scenarios (e.g., redirects,
valid/invalid board titles).
"""

import html

import pytest

from django.urls import reverse
from django.test import Client

from trello.views import CreateBoardView


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
class TestCreateBoardView:
    """Test the CreateBoardView class."""

    @pytest.fixture
    def client(self) -> Client:
        """
        Create a client instance to make requests.

        Returns:
            Client: A Django test client instance.
        """
        return Client()

    @pytest.fixture
    def view_instance(self) -> CreateBoardView:
        """
        Create an instance of the CreateBoardView.

        Returns:
            CreateBoardView: An instance of CreateBoardView.
        """
        return CreateBoardView()

    def test_get_context_data_default(
        self, view_instance: CreateBoardView
    ) -> None:
        """
        Test that get_context_data returns the default context.

        Args:
            view_instance (CreateBoardView): The view instance being tested.
        """
        context = view_instance.get_context_data()
        assert context == {"show_input": False, "message": None}

    def test_get_context_data_custom(
        self, view_instance: CreateBoardView
    ) -> None:
        """
        Test that get_context_data returns custom context values.

        Args:
            view_instance (CreateBoardView): The view instance being tested.
        """
        context = view_instance.get_context_data(
            show_input=True, message="Test Message"
        )
        assert context == {"show_input": True, "message": "Test Message"}

    def test_get_initial_page_load(self, client: Client) -> None:
        """
        Test that the page loads initially without the board title input.

        Args:
            client (Client): The Django test client.
        """
        url = reverse("create_board")
        response = client.get(url)

        # Check that the response status is 200 OK
        assert response.status_code == 200

        # Check that 'show_input' is in the context and its value is False
        assert response.context["show_input"] is False

    def test_post_show_input(self, client: Client) -> None:
        """
        Test that clicking 'Create' shows the input field for the board title.

        Args:
            client (Client): The Django test client.
        """
        url = reverse("create_board")

        # Simulate clicking the 'Create' button
        response = client.post(url, {"show_input": "true"})

        # Check that the input field is displayed after clicking 'Create'
        assert response.status_code == 200
        assert response.context["show_input"] is True

    def test_post_create_board_with_title(self, client: Client) -> None:
        """
        Test the creation of a board with a valid title.

        Args:
            client (Client): The Django test client.
        """
        url = reverse("create_board")

        # Simulate a POST request with a board title
        response = client.post(url, {"board_title": "My Board"})

        # Check that the response status is 200 OK
        assert response.status_code == 200

        # Decode the response content
        response_content = html.unescape(response.content.decode())

        # Expected message
        expected_message = "Transition to the board - 'My Board'"

        # Check that the expected message is in the response content
        assert expected_message in response_content

    def test_post_create_board_with_empty_title(self, client: Client) -> None:
        """
        Test that an error message is displayed when attempting to create a
        board with an empty title.

        Args:
            client (Client): The Django test client.
        """
        url = reverse("create_board")

        # Simulate a POST request with an empty title
        response = client.post(url, {"board_title": ""})

        # Check that the response status is 200 OK
        assert response.status_code == 200

        # Check if the error message is present in the response
        assert (
            "The board creation button is not active until there is no name!"
            in response.content.decode()
        )
