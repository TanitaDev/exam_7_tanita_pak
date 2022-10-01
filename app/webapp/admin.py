from django.contrib import admin

from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mail', 'text', 'create_at', 'updated_at', 'status']


admin.site.register(GuestBook, GuestBookAdmin)
