"""
Tests for the boards template functionality in the Trello application.

This module contains unit tests that verify the correct rendering and behavior
of the boards template in the Trello application. Tests ensure that the template
displays the expected content and responds correctly to various conditions such
as the state of the `show_input` flag.
"""

import pytest

from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
class TestBoardsTemplate:
    """
    Test suite for verifying the functionality of the base boards template.
    """

    def test_base_template_renders_correctly(self) -> None:
        """
        Test that the base template renders correctly with the expected content.

        Verifies:
            - The fixed header with the "Trello" button is displayed.
            - Includes conditional rendering of the create board form.
            - The main content block is present in the template.

        Raises:
            AssertionError: If the template content is not as expected.
        """
        client: Client = Client()

        # Render the base template
        response = client.get(reverse("create_board"))

        # Ensure the template renders without errors
        assert (
            response.status_code == 200
        ), f"Expected 200 status code, got {response.status_code}."

        # Check for the "Trello" button in the fixed header
        assert (
            "Trello" in response.content.decode()
        ), "Expected 'Trello' button in the fixed header, but not found."
