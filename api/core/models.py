# core/models.py

from django.db import models
# Create your models here.

class Sport(models.Model):
    DIFFICULTY_LEVELS = (
        ('Robert Pitt', 'Robert Pitt'),
        ('Sam Venom', 'Sam Venom'),
        ('Daniel John', 'Daniel John'),
    )
    name = models.CharField(max_length=120)
    definition = models.CharField(max_length=400)
    image = models.FileField()
    author = models.CharField(choices=DIFFICULTY_LEVELS, max_length=20)
    realized = models.TextField()

    def __str_(self):
        return "Sport for {}".format(self.name)