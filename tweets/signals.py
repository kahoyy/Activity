from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tweet
from history.models import History

@receiver(post_save, sender=Tweet)
def create_history_on_tweet(sender, instance, created, **kwargs):
    if created:
        History.objects.create(
            user=instance.user,
            method="POST",
            tweet=instance,
            summary=f"User {instance.user.username} Created tweet with a content of '{instance.content}' at {instance.created_at}"
        )
