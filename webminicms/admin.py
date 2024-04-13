from django.contrib import admin
from cms_content.models import TextContent, MediaContent
from cms_users.models import AppUsers

admin.site.register(TextContent)
admin.site.register(MediaContent)
admin.site.register(AppUsers)
