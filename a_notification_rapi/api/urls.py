from .views import NotificationListCreateAPIView
from django.urls import path, include


urlpatterns = [
    path('', NotificationListCreateAPIView.as_view(), name = "notification"),
]