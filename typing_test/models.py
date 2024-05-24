from django.db import models


class TypingText(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

