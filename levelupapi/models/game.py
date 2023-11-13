from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    name = models.CharField(max_length=200)
    max_players = models.PositiveIntegerField()
    image = models.URLField(null=True, blank=True)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="games")
    gamer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="games_created")