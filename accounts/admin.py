from django.contrib import admin
from .models import UserAccount


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "first_name", "last_name",
                    "phone_number", "is_active", "is_staff",)
    search_fields = ("email", "username", "first_name", "last_name",
                     "phone_number",)


admin.site.register(UserAccount, UserAccountAdmin)
