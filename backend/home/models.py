from django.conf import settings
from django.db import models


class Message(models.Model):
    "Generated Model"
    match = models.ForeignKey(
        "dating.Match",
        on_delete=models.CASCADE,
        related_name="message_match",
    )
    slug = models.SlugField(
        max_length=50,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )
    inbox = models.ForeignKey(
        "dating.Inbox",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="message_inbox",
    )


class CustomText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=150,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()
