"""
URL configuration for trello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path
from trello.views import CreateBoardView, redirect_to_boards, BoardDetailView

urlpatterns = [
    path("", redirect_to_boards, name="redirect_to_boards"),
    path("admin/", admin.site.urls),
    path("boards/", CreateBoardView.as_view(), name="create_board"),
    path(
        "boards/<str:board_title>/",
        BoardDetailView.as_view(),
        name="board_detail",
    ),
]
