from django.db import models
from accounts.models import UserProfile
from cataloge.models import Film


class Review(models.Model):
    film = models.ForeignKey(
        Film, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
