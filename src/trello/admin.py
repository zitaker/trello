"""
Django admin module for the Trello app.
"""

from django.contrib import admin
from trello.models import Board


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    """
    Admin class for `Board` model.

    Attributes:
        list_display (tuple): Fields to display in the list view of the model.
    """

    list_display: tuple[str, str] = ("title", "created_at")
