from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# Workout Model
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


# Exercise Model
class Exercise(models.Model):
    # Muscle List will allow for users to sort through exercises based on desired muslce activation
    MUSCLES = [
        ('abductors','Abductors'), ('abdominals','Abdominals'), ('adductors','Adductors'),
        ('biceps','Biceps'), ('brachialis','Brachialis'), ('calves','Calves'),
        ('chest','Chest'), ('forearms','Forearms'), ('front_deltoid','Front Deltoid'),
        ('glutes','Glutes'), ('hamstrings','Hamstrings'), ('lateral_deltoid','Lateral Deltoid'),
        ('lats','Lats'), ('lower_back','Lower Back'), ('obliques','Obliques'),
        ('quads','Quads'), ('rear_deltoid','Rear Deltoid'), ('sternocleidomastoid','Sternocleidomastoid'),
        ('traps','Traps'), ('triceps','Triceps'), ('upper_chest','Upper Chest')
    ]
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null= True,
        blank= True,
        related_name='custom_exercise')

    name = models.CharField(max_length=100)
    primary_muscle = models.CharField(max_length=50, choices= MUSCLES)
    secondary_muscle = models.CharField(max_length=50, choices=MUSCLES)
    equipment = models.CharField(max_length=50, choices=[('bodyweight','Body Weight'),('freeweight','Free Weight'),
                                                         ('machine','Machine')])

    class Meta:
        unique_together = ('name', 'created_by')
        ordering = ['name']
    def __str__(self):
        creator = self.created_by.username if self.created_by else "Default"
        return f"{self.name} ({creator})"