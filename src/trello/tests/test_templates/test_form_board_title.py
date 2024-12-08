"""
This module contains tests to ensure that the form for creating a new board
title is functioning correctly. The tests include verifying that the form
renders as expected and that submitting the form processes correctly,
displaying the expected elements and result.

The tests include:
- Rendering checks for the initial form view.
- Verification of the extended form view after form submission.
"""

import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
class TestFormBoardTitle:
    """Test suite for the form used to create a new board title."""

    # pylint: disable=R0801
    def __init__(self) -> None:
        """Initialize the Django test client."""
        self.client: Client = Client()

    def test_get_initial_form(self) -> None:
        """
        Test that the form for creating a new board title renders correctly.

        This verifies that the form is properly displayed with the expected
        fields and a "Create" button.
        """
        url: str = reverse("create_board")
        response = self.client.get(url)
        assert response.status_code == 200
        content: str = response.content.decode("utf-8")
        assert (
            '<button type="submit" name="show_input" value="true">'
            "Create</button>" in content
        )

    # pylint: enable=R0801

    def test_post_show_extended_form(self) -> None:
        """
        Test that submitting the form for creating a new board title works
        correctly.

        This checks that after submitting the form with the board title, the
        extended form with the title field and "Create" button is rendered.
        """
        url: str = reverse("create_board")
        response = self.client.post(url, {"show_input": "true"})
        assert response.status_code == 200
        content: str = response.content.decode("utf-8")
        assert '<label for="board_title">' in content
        assert '<input type="text" id="board_title"' in content
        assert '<button type="submit">Create</button>' in content
