"""
Tests for checking the correctness of URL routing in the application.

This module contains tests for the URL patterns in the Django application.
It verifies that the URLs correctly resolve to the expected views and that
they return the appropriate HTTP status codes. The tests ensure that the
application's routing behaves as expected and helps catch potential issues
with URL configuration.
"""

import pytest

from django.urls import reverse
from django.test import Client

from trello.models import Board


@pytest.mark.django_db
class TestUrlsBoards:
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
        assert response.url == reverse("create_board")  # Expecting redirect

    def test_create_board_url(self, client) -> None:
        """
        Test that the '/boards/' URL maps to
        the CreateBoardView class-based view.

        This test verifies that the URL for the boards page correctly resolves
        to the `CreateBoardView` view.

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


@pytest.mark.django_db
class TestAdminURL:
    """
    Test suite for verifying the accessibility of the Django admin URL.
    """

    def test_admin_url_accessibility(self) -> None:
        """
        Test that the `/admin/` URL is accessible and returns a 200 status code.

        Verifies:
            - The `/admin/` URL is configured correctly in `urlpatterns`.
            - The URL returns the correct HTTP status code (200 or 302).

        Raises:
            AssertionError: If the status code is not as expected.
        """
        client: Client = Client()

        # Reverse the admin URL to ensure it's correctly named (if applicable)
        url = reverse("admin:index")

        # Make a GET request to the admin URL
        response = client.get(url)

        # Admin requires authentication, so expect a redirect (302)
        assert response.status_code == 302, (
            f"Expected 302 status code for unauthenticated admin access, "
            f"got {response.status_code}."
        )

        # Check the redirection URL (usually login page)
        assert (
            "/admin/login/" in response.url
        ), "Unauthenticated access to admin did not redirect to login page."


@pytest.mark.django_db
class TestBoardDetailURL:
    """
    Test suite for verifying the functionality of the `board_detail` URL.
    """

    def test_board_detail_url(self) -> None:
        """
        Test that the `board_detail` URL works correctly and returns a 200
        status code for an existing board.

        Verifies:
            - The `board_detail` URL resolves and is accessible.
            - The correct board details are displayed in the response.

        Raises:
            AssertionError: If the status code or response content is
                unexpected.
        """
        client: Client = Client()

        # Create a test board instance
        board: Board = Board.objects.create(title="test_board")

        # Reverse the URL with the board's title
        url = reverse("board_detail", kwargs={"board_title": board.title})

        # Make a GET request to the board detail URL
        response = client.get(url)

        # Check that the status code is 200
        assert (
            response.status_code == 200
        ), (
            "Expected 200 status code for board detail page, got ",
            f" {response.status_code}."
        )

        # Check that the board title appears in the response content
        assert (
            board.title in response.content.decode()
        ), "Board title not found in the response content."
