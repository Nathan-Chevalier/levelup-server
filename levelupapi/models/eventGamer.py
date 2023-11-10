from django.db import models
from django.contrib.auth.models import User

class EventGamer(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="gamer_events")
    gamer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_gamers")
    timestamp = models.DateTimeField(auto_now_add=True)