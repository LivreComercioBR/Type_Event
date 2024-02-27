from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.


@admin.register(User)
class AdminUserAdmin(UserAdmin):
    list_display = ('username', 'email', )
    list_filter = ('username', 'email',)
    list_editable = ('email', )
