from django.db import models


class TypingText(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        permissions = [
            ("can_add_text", "Can add typing text"),
            ("can_change_text", "Can change typing text"),
        ]

