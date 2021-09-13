from django.contrib import admin
from .models import Message

# Register your models here.

admin.site.site_header = "Portfolio | Admin panel"
admin.site.site_title = "Portfolio | Admin panel"
admin.site.index_title = "Portfolio | Admin panel"

admin.site.register(Message)