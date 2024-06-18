from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class APIKey(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)


class BotSettings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crypto = models.CharField(max_length=10)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2)
    pyramiding_level = models.DecimalField(max_digits=5, decimal_places=2)
    rebuy_option = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
