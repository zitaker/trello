"""
Unit tests for the board creation functionality in the 'boards.html' template.

These tests cover the behavior of the board creation page, ensuring that:

1. The page loads correctly without the 'show_input' field displayed.
2. The page loads with the 'show_input' field when appropriate data is posted.
3. The page is loaded from "YOUR WORKSPACES".
"""

import pytest

from django.urls import reverse
from django.test import Client

from trello.models import Board


@pytest.mark.django_db
class TestBoardsTemplate:
    """Test the rendering of the boards template."""

    @pytest.fixture
    def client(self) -> Client:
        """Create a client instance to make requests.

        Returns:
            Client: A Django test client to make HTTP requests.
        """
        return Client()

    def test_boards_page_loads_without_show_input(self, client: Client) -> None:
        """
        Test that the boards page loads with the correct template and context.

        This test ensures that the board creation page loads with the
        'show_input' variable set to False when no data is posted.

        Args:
            client (Client): The Django test client used for making requests.
        """
        url = reverse("create_board")  # Use the correct route name
        response = client.get(url)

        # Ensure the status code is 200 (OK)
        assert response.status_code == 200

        # Ensure the correct template is used
        assert "boards.html" in [
            template.name for template in response.templates
        ]

        # Ensure the context contains 'show_input' with value False
        assert response.context["show_input"] is False

    def test_boards_page_loads_with_show_input(self, client: Client) -> None:
        """Test that the boards page loads with the correct template and context
        when show_input is True.

        This test simulates posting data to activate 'show_input', ensuring the
        correct template and context values are returned.

        Args:
            client (Client): The Django test client used for making requests.
        """
        url = reverse("create_board")  # URL for the boards page

        # Send data to activate show_input
        response = client.post(url, data={"show_input": "true"})

        # Ensure the status code is 200 (OK)
        assert response.status_code == 200

        # Ensure the correct template is used
        assert "boards.html" in [
            template.name for template in response.templates
        ]

        # Ensure the context contains 'show_input' with value True
        assert response.context["show_input"] is True

    def test_boards_list_displayed(self, client: Client) -> None:
        """
        Test that the boards are correctly listed on the boards page.

        This test checks that all boards in the context are displayed in an
        unordered list within the 'boards.html' template.

        Args:
            client (Client): The Django test client used for making requests.
        """
        # Create some boards for testing
        Board.objects.create(title="Board 1")
        Board.objects.create(title="Board 2")

        url = reverse("create_board")  # URL for the boards page
        response = client.get(url)

        # Ensure the status code is 200 (OK)
        assert response.status_code == 200

        # Ensure the correct template is used
        assert "boards.html" in [
            template.name for template in response.templates
        ]

        # Ensure the context contains boards
        boards = response.context["boards"]
        assert len(boards) == 2

        # Ensure the boards are listed
        assert any("Board 1" in str(board) for board in boards)
        assert any("Board 2" in str(board) for board in boards)

    def test_boards_header_displayed(self, client: Client) -> None:
        """
        Test that the header and boards list are displayed on the boards page.

        This test checks that the boards page displays the 'YOUR WORKSPACES'
        header and lists existing boards in an unordered list.

        Args:
            client (Client): Django test client for requests.
        """
        # Create some boards for testing
        Board.objects.create(title="Board 1")
        Board.objects.create(title="Board 2")

        url = reverse("create_board")  # URL for the boards page
        response = client.get(url)

        assert response.status_code == 200

        # Ensure the correct template is used
        assert "boards.html" in [
            template.name for template in response.templates
        ]

        # Check the page header
        assert "<h3>YOUR WORKSPACES</h3>" in response.content.decode()

        # Check the boards list display
        boards_list = (
            response.content.decode().split("<ul>")[1].split("</ul>")[0]
        )
        assert "Board 1" in boards_list
        assert "Board 2" in boards_list
