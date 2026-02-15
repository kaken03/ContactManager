from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'phone', 'category', 'is_favorite', 'created_at')
    list_filter = ('category', 'is_favorite', 'created_at')
    search_fields = ('name', 'email', 'phone')
    readonly_fields = ('created_at',)
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Contact Information', {
            'fields': ('name', 'phone', 'email', 'address')
        }),
        ('Organization', {
            'fields': ('category', 'is_favorite')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
