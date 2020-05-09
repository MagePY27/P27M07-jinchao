from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('name', 'username')
    filter_horizontal = ('user_permissions', 'groups',)
    list_per_page = 10

    fieldsets = (
        (None, {'fields': ('username','password')}),
        ('基本信息', {'fields': ('name','email','phone')}),
        ('用户权限', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions','groups')}),
        ('日期', {'fields': ('last_login', 'date_joined')}),
    )
