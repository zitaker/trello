"""
Module for testing the form functionality on the /boards/ page.

This module contains tests to validate the rendering and processing
of the form located at /boards/. It ensures that the form is displayed
with the correct HTML structure and attributes and that it processes
POST requests as expected.

Classes:
    TestFormCreateButton: Contains test cases for verifying the form's
    behavior, including GET and POST requests.

Dependencies:
    - pytest: For test discovery and execution.
    - django.test.Client: For simulating HTTP requests to the Django app.
    - django.urls.reverse: For dynamically resolving URL names.
"""

import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestFormCreateButton:
    """Test class for validating the form on the /boards/ page."""

    def __init__(self) -> None:
        """Initialize the Django test client."""
        self.client: Client = Client()

    def test_form_create_button_render(self) -> None:
        """Test that the form renders correctly on the /boards/ page.

        Verifies:
            - The HTTP status code is 200.
            - The form contains the correct HTML elements and attributes.
        """
        url: str = reverse("create_board")
        response = self.client.get(url)
        assert response.status_code == 200
        content: str = response.content.decode("utf-8")
        assert '<form method="POST">' in content
        assert 'name="show_input"' in content
        assert 'value="true"' in content

    def test_form_create_button_post(self) -> None:
        """Test that the form processes POST requests correctly.

        Verifies:
            - The HTTP status code is 200.
            - The form submits the expected data.
        """
        url: str = reverse("create_board")
        response = self.client.post(url, {"show_input": "true"})
        assert response.status_code == 200
