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

import pytest

from django.urls import reverse
from django.test import Client

from django.db.models.query import QuerySet

from trello.models import Board
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

    def test_get_context_data_default(self) -> None:
        """
        Test that `get_context_data` returns the default context.

        Verifies that the context dictionary contains the expected
        keys with their default values, and ensures that the 'boards'
        key is of type `QuerySet`.

        Returns:
            None
        """
        view_instance = CreateBoardView()  # Create a view instance.
        context = view_instance.get_context_data()

        # Verify the presence of keys in the context
        assert "show_input" in context
        assert "message" in context
        assert "boards" in context

        # Verify default values
        assert context["show_input"] is False
        assert context["message"] is None
        assert isinstance(context["boards"], QuerySet)

    def test_get_context_data_custom(
        self, view_instance: CreateBoardView
    ) -> None:
        """
        Test that `get_context_data` returns custom context values.

        Args:
            view_instance (CreateBoardView): The view instance being tested.
        """
        context = view_instance.get_context_data(
            show_input=True, message="Test Message"
        )

        # Check that the context contains the expected keys and their values
        assert "show_input" in context
        assert context["show_input"] is True
        assert "message" in context
        assert context["message"] == "Test Message"

        # Ensure boards is a list (empty list in this case)
        boards_list = list(context["boards"])
        assert isinstance(boards_list, list)
        assert len(boards_list) == 0  # Check that the list is empty as expected

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
        response = client.post(url, {"board_title": "My_Board"})

        # Check that the response status is 302 Found (redirected)
        assert response.status_code == 302

        # Redirect URL should point to the new board's detail page
        expected_url = "/boards/My_Board/"
        assert response.url == expected_url

        # Check that the URL in the response matches the expected URL
        assert response.url == expected_url


class TestBoardDetailView:
    """Test case for the `BoardDetailView`."""

    @pytest.mark.django_db
    def test_get_board_detail_view(self) -> None:
        """
        Test that `BoardDetailView` works as expected.

        This test checks if the view correctly displays a specific board
        when accessed via its title.

        It creates a sample board, sends a GET request to the view,
        and asserts that the response status is 200 and the board title
        is included in the response content.

        Raises:
            AssertionError: If the response status is not 200 or
                            the board title is not in the response content.
        """
        # Arrange: Create a sample board for testing
        board = Board.objects.create(title="test_board")

        # Setup
        client = Client()
        url = reverse("board_detail", args=[board.title])

        # Act
        response = client.get(url)

        # Assert
        assert (
            response.status_code == 200
        ), f"Expected status code 200 but got {response.status_code}"
        assert (
            "test_board" in response.content.decode()
        ), "Board title is not present in the response."
