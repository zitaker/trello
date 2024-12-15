"""
Module for testing the rendering of Django templates.

This module includes test cases for verifying that templates render correctly
with the expected context data. It uses pytest for test organization and
django's template rendering tools.

Classes:
    TestBoardTemplate: Test suite for the board detail template.
"""

import pytest


from django.test import RequestFactory
from django.template.loader import render_to_string


@pytest.mark.django_db
class TestBoardTemplate:
    """
    Test class for verifying the rendering of the board detail template.
    """

    def test_board_template_rendering(self) -> None:
        """
        Tests that the board detail template renders correctly with the provided
        context data.

        Assertions:
            - The board title is displayed in the template.
        """
        # Prepare test data
        board: object = type("Board", (object,), {"title": "Test Board"})()
        request = RequestFactory().get("/")

        # Render the template
        rendered_template: str = render_to_string(
            template_name="board_detail.html",
            context={"board": board},
            request=request,
        )

        # Assert that the board title is in the template
        assert (
            "Test Board" in rendered_template
        ), "The board title is not displayed in the template."
