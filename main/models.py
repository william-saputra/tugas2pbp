from django.db import models

# Create your models here.
class LeatherStore(models.Model):
    name = models.CharField(max_length=70)
    price = models.IntegerField()
    description = models.TextField(max_length=2000)
    thickness = models.DecimalField(max_digits=4, decimal_places=2)
    user_reviews = models.TextField(max_length=1000)

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5