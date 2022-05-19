from django.db import models

class Event_Gamer(models.Model):
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    event = modes.ForeingKey(Event, on_delete=models.CASCADE)