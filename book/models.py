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

    # def save(self, *args, **kwargs):
    #     super(Bet, self).save(*args, **kwargs)


class BaseballLine(models.Model):
    gamekey = models.CharField(max_length=255, primary_key=True)
    eventtime = models.DateTimeField()
    vteam = models.CharField(max_length=255)
    vpitcher = models.CharField(max_length=255)
    vrot = models.IntegerField(null=True)
    hteam = models.CharField(max_length=255)
    hpitcher = models.CharField(max_length=255)
    hrot = models.IntegerField(null=True)
    periodnum = models.IntegerField(null=True)
    perioddesc = models.CharField(max_length=255, null=True)
    vml = models.IntegerField(null=True)
    hml = models.IntegerField(null=True)
    vspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    vodds = models.IntegerField(null=True)
    hspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    hodds = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    overodds = models.IntegerField(null=True)
    underodds = models.IntegerField(null=True)
    lastupdated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return str(self.vteam) + ' at ' + str(self.hteam) + ' ' + str(self.eventtime)


class BasketballLine(models.Model):
    gamekey = models.CharField(max_length=255, primary_key=True)
    eventtime = models.DateTimeField()
    vteam = models.CharField(max_length=255)
    vrot = models.IntegerField(null=True)
    hteam = models.CharField(max_length=255)
    hrot = models.IntegerField(null=True)
    periodnum = models.IntegerField(null=True)
    perioddesc = models.CharField(max_length=255)
    vml = models.IntegerField(null=True)
    hml = models.IntegerField(null=True)
    vspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    vodds = models.IntegerField(null=True)
    hspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    hodds = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    overodds = models.IntegerField(null=True)
    underodds = models.IntegerField(null=True)
    lastupdated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return str(self.vteam) + ' at ' + str(self.hteam) + ' ' + str(self.eventtime)


class FootballLine(models.Model):
    gamekey = models.CharField(max_length=255, primary_key=True)
    eventtime = models.DateTimeField()
    vteam = models.CharField(max_length=255)
    vrot = models.IntegerField(null=True)
    hteam = models.CharField(max_length=255)
    hrot = models.IntegerField(null=True)
    periodnum = models.IntegerField(null=True)
    perioddesc = models.CharField(max_length=255)
    vml = models.IntegerField(null=True)
    hml = models.IntegerField(null=True)
    vspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    vodds = models.IntegerField(null=True)
    hspread = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    hodds = models.IntegerField(null=True)
    total = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    overodds = models.IntegerField(null=True)
    underodds = models.IntegerField(null=True)
    lastupdated = models.DateTimeField(auto_now=True, editable=False)

    def __unicode__(self):
        return str(self.vteam) + ' at ' + str(self.hteam) + ' ' + str(self.eventtime)
