from django.contrib import admin
from .models import CustomUser, UserToNotification, ActionSubscription

admin.site.register(CustomUser)
admin.site.register(UserToNotification)
admin.site.register(ActionSubscription)
