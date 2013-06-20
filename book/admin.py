from django.contrib import admin
from .models import Bet, BaseballLine, BasketballLine, FootballLine

admin.site.register(Bet)
admin.site.register(BasketballLine)
admin.site.register(BaseballLine)
admin.site.register(FootballLine)
