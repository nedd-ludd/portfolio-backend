from django.urls import path
from .views import ContactListView

urlpaterns = [
    path('', ContactListView.as_view()),
]