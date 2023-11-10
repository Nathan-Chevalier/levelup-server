from django.db import models
from django.contrib.auth.models import User

class EventGamer(models.Model):
    event = models.ForeignKey("Event", on_delete=models.CASCADE)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)