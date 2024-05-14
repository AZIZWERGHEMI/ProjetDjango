# views.py

from django.shortcuts import render, redirect
from .models import Notification  # Importing Notification from the correct location

def ShowNotification(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-date')

    context = {
        'notifications': notifications,
    }
    return render(request, 'Notification.html', context)

def DeleteNotification(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, user=user).delete()
    return redirect('show-notification')
