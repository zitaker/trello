"""This module contains models for the Trello application."""

from django.db import models


class Board(models.Model):
    """
    Model representing a board.

    Attributes:
        title (str): The title of the board.
        created_at (datetime): The date and time when the board was created.
    """

    title: models.CharField = models.CharField(max_length=255, unique=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Return a string representation of the board.

        Returns:
            str: The title of the board.
        """
        return str(self.title)
