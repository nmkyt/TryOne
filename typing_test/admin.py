from django.contrib import admin
from django.contrib.auth.models import Group
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import TypingText


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class UserAdmin(BaseUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(TypingText)
class TypingTextAdmin(admin.ModelAdmin):
    list_display = ('content',)
    actions = ['assign_to_moderator']

    def assign_to_moderator(self, request, queryset):
        moderator_group = Group.objects.get(name='Moderator')
        for user in queryset:
            user.groups.add(moderator_group)
        self.message_user(request, "Selected users have been assigned to Moderator group")
    assign_to_moderator.short_description = "Assign to Moderator group"
