from django.db import models

class Game(models.Model):
    game_type = models.ForeignKey(Game_Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    maker = models.CharField(max_length=20)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.IntegerField(default='0', blank=False)
    skill_level = models.IntegerField(default='0', blank=False)