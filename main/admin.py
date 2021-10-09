from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time', 'number', 'text', 'list')


admin.site.register(Record, RecordAdmin)
