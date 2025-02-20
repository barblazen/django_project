from django.contrib import admin

# Register your models here.
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "registration_date","id",'is_active')
    actions = ("activate_all_users",)
    @admin.action(description= "Activate all users")
    def activate_all_users(self, request, queryset):
        queryset.update(is_active=True)



