
from django.urls import path
from .views import ShowNotification, DeleteNotification  # Importing views from the correct location

urlpatterns = [
    path('', ShowNotification, name='show-notification'),
    path('<noti_id>/delete', DeleteNotification, name='delete-notification'),
]
