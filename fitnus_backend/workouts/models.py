from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workouts')
    date = models.DateField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    total_volume_kilograms = models.FloatField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    is_public = models.BooleanField(default=False)
    title = models.CharField(max_length=100, blank=True, default='My Workout')
    notes = models.TextField(blank=True, default='')

    def __str__(self):
        return f"{self.title} ({self.user.username})"