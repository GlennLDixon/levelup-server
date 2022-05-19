from django.db import models

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)