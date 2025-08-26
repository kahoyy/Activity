from django.db import models
from django.contrib.auth.models import User
from tweets.models import Tweet

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=10)  # e.g., "POST"
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.method} - {self.date}"

# Create your models here.
