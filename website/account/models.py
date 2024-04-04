
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    telegram_id = models.BigIntegerField(null=True)
    subscription = models.TimeField(max_length=80, null=True)
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






class News(models.Model):
    title = models.CharField(max_length=80)
    photo = models.ImageField(upload_to='static/images', null=True)
    article = models.TextField()
    category = models.TextField()
    time = models.DateTimeField()














































