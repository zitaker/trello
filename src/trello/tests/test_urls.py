"""
Tests for checking the correctness of URL routing in the application.

This module contains tests for the URL patterns in the Django application.
It verifies that the URLs correctly resolve to the expected views and that
they return the appropriate HTTP status codes. The tests ensure that the
application's routing behaves as expected and helps catch potential issues
with URL configuration.

Tests include:
- Checking redirection from the home page to the boards page.
- Ensuring the '/boards/' URL resolves to the correct view.

Modules used:
- pytest: For testing framework and fixtures.
- django.urls: For reverse URL resolution.
- django.test.Client: For simulating HTTP requests.
"""

import pytest

from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestUrls:
    """Tests for checking the correctness of URL routing in the app."""

    @pytest.fixture
    def client(self) -> Client:
        """Fixture that provides a test client for sending requests.

        Returns:
            Client: The test client for making HTTP requests.
        """
        return Client()

    def test_redirect_to_boards_url(self, client) -> None:
        """Test that a request to the home page ("/") redirects to /boards/.

        This test checks if the home page correctly redirects to the boards
        page.

        Args:
            client (Client): The test client for sending requests.

        Returns:
            None
        """
        url = reverse("redirect_to_boards")  # URL name for the home page
        response = client.get(url)
        assert response.status_code == 302  # Expecting a redirect
        assert response.url == reverse(
            "create_board"
        )  # Expecting redirect to /boards/

    def test_create_board_url(self, client) -> None:
        """Test that the '/boards/' URL maps to the create_board view.

        This test verifies that the URL for the boards page correctly resolves
        to the `create_board` view.

        Args:
            client (Client): The test client for sending requests.

        Returns:
            None
        """
        url = reverse("create_board")  # Using the route name for /boards/
        response = client.get(url)
        assert (
            response.status_code == 200
        )  # Expecting status 200 OK for the page
