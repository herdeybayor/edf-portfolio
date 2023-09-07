from django.contrib import admin
from .models import Script, Website, API, Certificate, Message


class APIAdmin(admin.ModelAdmin):
    list_display = ('api_type', 'name', 'image', 'description', 'url')


class ScriptAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'url')


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'fm_type', 'url')


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'date', 'source')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')


admin.site.register(Script, ScriptAdmin)
admin.site.register(Website, WebsiteAdmin)
admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Message)
admin.site.register(API, APIAdmin)
