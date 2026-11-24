from django.db import models
from django.contrib.auth.models import User


class FoodDiaryDb(models.Model):

    MEAL_CHOICES = [
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snacks', 'Snacks'),
        ('Dinner', 'Dinner'),
    ]

    food_name = models.CharField(max_length=100)
    meal_type = models.CharField(max_length=20,choices=MEAL_CHOICES)
    quantity = models.CharField(max_length=100)
    calories = models.IntegerField()
    meal_date = models.DateField()
    notes = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.food_name

class WeightTrackerDb(models.Model):
    weight=models.FloatField()
    recorded_date=models.DateField()
    notes=models.TextField(null=True,blank=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

def __str__(self):
    return f"{self.weight} kg - {self.recorded_date}"