from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from typing_test.models import TypingText


class Command(BaseCommand):
    help = 'Create user groups and permissions'

    def handle(self, *args, **kwargs):

        moderator_group, created = Group.objects.get_or_create(name='Moderator')

        content_type = ContentType.objects.get_for_model(TypingText)

        add_text_permission, created = Permission.objects.get_or_create(
            codename='add_text',
            name='Can add typing text',
            content_type=content_type,
        )

        change_text_permission, created = Permission.objects.get_or_create(
            codename='change_text',
            name='Can change typing text',
            content_type=content_type,
        )

        # Assign permissions to groups
        moderator_group.permissions.add(add_text_permission)
        moderator_group.permissions.add(change_text_permission)

        self.stdout.write(self.style.SUCCESS('Successfully created groups and assigned permissions'))
