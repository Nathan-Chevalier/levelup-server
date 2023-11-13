from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events_created")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=200)
    attendees = models.ManyToManyField(User, through="EventGamer", related_name="events")
    event_time = models.DateTimeField()
    event_location = models.CharField(max_length=2000)