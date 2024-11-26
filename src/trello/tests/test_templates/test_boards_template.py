"""
Unit tests for the board creation functionality in the 'boards.html' template.

These tests cover the behavior of the board creation page, ensuring that:

1. The page loads correctly without the 'show_input' field displayed.
2. The page loads with the 'show_input' field when appropriate data is posted.
3. No message is displayed when no message is set in the context.

Tests are implemented using the pytest framework and Django's test client.

Modules:
    pytest: Testing framework used for unit tests.
    django.urls.reverse: Utility for generating URL patterns from view names.
    django.test.Client: Django's test client used for simulating HTTP requests.

Test Methods:
    - test_boards_page_loads_without_show_input: Verifies that the board page
      loads correctly with 'show_input' set to False.
    - test_boards_page_loads_with_show_input: Verifies that the board page
      loads correctly with 'show_input' set to True after posting data.
    - test_no_message: Verifies that no message is shown when the 'message'
      context is not set.

"""

import pytest

from django.urls import reverse
from django.test import Client


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

        This test ensures that the board creationpage loads with the
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

    def test_no_message(self, client: Client) -> None:
        """
        Test that no message is displayed if the 'message'
        context is not passed.

        This test checks that when no message is set in the context, it does not
        appear in the response.

        Args:
            client (Client): The Django test client used for making requests.
        """
        url = reverse("create_board")  # URL for the boards page
        response = client.get(url)

        # Ensure the status code is 200 (OK)
        assert response.status_code == 200

        # Ensure there is no message in the response content
        assert "message" not in response.content.decode()
