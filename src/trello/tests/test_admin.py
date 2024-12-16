"""
Tests for the Django admin configuration of the Trello app.

This module contains test cases for ensuring that the `BoardAdmin` class in
the Django admin interface is correctly registered and configured. The tests
focus on verifying the registration of the `Board` model and the proper
configuration of attributes such as `list_display`.

Classes:
    TestBoardAdmin: Contains test cases for the `BoardAdmin` class.

Dependencies:
    - pytest for testing.
    - Django's admin and model modules.
"""

import pytest

from django.contrib.admin import site

from trello.models import Board
from trello.admin import BoardAdmin


@pytest.mark.django_db
class TestBoardAdmin:
    """
    Test suite for the BoardAdmin class in the Django admin interface.
    """

    def test_board_admin_registered(self) -> None:
        """
        Test that the `Board` model is registered in the Django admin site.

        Verifies:
            - The `Board` model is registered in the admin site.
            - The `Board` model is associated with the correct admin class.

        Raises:
            AssertionError: If the `Board` model is not registered or if the
                associated admin class is not `BoardAdmin`.
        """
        # Ensure the model is registered
        assert site.is_registered(
            Board
        ), "Board model is not registered in admin."  # pylint: disable=W0212

        # Ensure the correct admin class is used
        assert isinstance(
            site._registry[Board],  # pylint: disable=W0212
            BoardAdmin,
        ), "Board model is not associated with BoardAdmin class."

    def test_board_admin_list_display(self) -> None:
        """
        Test that the `list_display` attribute of `BoardAdmin` is configured
        correctly.

        Verifies:
            - The `list_display` attribute contains the expected fields.

        Raises:
            AssertionError: If `list_display` does not match the expected
                configuration.
        """
        expected_display: tuple[str, str] = ("title", "created_at")
        assert (
            BoardAdmin.list_display == expected_display
        ), "list_display does not match the expected fields."
