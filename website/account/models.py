
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telegram_id = models.BigIntegerField()
    subscription = models.TimeField(max_length=80)
    #photo = models.ImageField()
    # Добавление параметра related_name для избежания конфликта имен
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )


"""class Notification(models.Model):
    action_name = models.CharField(max_length=80)
    price_change = models.FloatField()
    day_price_change = models.FloatField()
    price = models.FloatField()
    volume_lots = models.IntegerField()
    volume_rub = models.IntegerField()
    buy = models.IntegerField()
    sell = models.IntegerField()
    Z_deviation = models.FloatField()
    time = models.TimeField()"""


class UserToNotification(models.Model):
    user_id = models.BigIntegerField()
    notification_id = models.BigIntegerField()


class ActionSubscription(models.Model):
    action_id = models.BigIntegerField()
    Z_deviation = models.FloatField()














































