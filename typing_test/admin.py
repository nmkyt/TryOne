from django.contrib import admin
from typing_test.models import TypingText


@admin.register(TypingText)
class TypingTextAdmin(admin.ModelAdmin):
    pass

