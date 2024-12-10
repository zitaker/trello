"""
Tests for the Board model in the Trello application.

These tests validate the correct behavior of the Board.
"""

from django.test import TestCase
from django.utils import timezone
from trello.models import Board


class TestBoardModel(TestCase):
    """Test the creation of a Board."""

    def test_board_creation(self) -> None:
        """Test the creation of a Board."""
        title = "Test Board"
        board = Board(title=title)
        board.save()

        self.assertEqual(board.title, title)
        self.assertIsInstance(
            board.created_at, timezone.datetime  # type: ignore
        )

    def test_board_unique_title(self) -> None:
        """Test that a Board's title must be unique."""
        title = "Unique Board"
        board = Board(title=title)
        board.save()

        with self.assertRaises(Exception) as context:
            board = Board(title=title)
            board.save()

        # Check if the exception message contains a
        # unique constraint error message
        self.assertTrue(
            "unique constraint" in str(context.exception).lower()
            or "duplicate key" in str(context.exception).lower()
        )
