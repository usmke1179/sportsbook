from django.contrib.auth.models import User
from django.db import models


class Bet(models.Model):
    user = models.ForeignKey(User, related_name="bets")
    sport = models.CharField(max_length=255)
    eventtime = models.DateTimeField()
    bet_type = models.CharField(max_length=255)
    bet_desc = models.CharField(max_length=255)
    risk = models.DecimalField(max_digits=5, decimal_places=2)
    to_win = models.DecimalField(max_digits=5, decimal_places=2)
    result = models.CharField(max_length=255)
    net = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    # def save(self, *args, **kwargs):
    #     super(Bet, self).save(*args, **kwargs)
