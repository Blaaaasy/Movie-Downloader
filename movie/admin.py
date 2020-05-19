from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Categroys)
class CategroysAdmin(admin.ModelAdmin):
    list_display = ('id', 'categroy')


@admin.register(models.M_info)
class M_infoAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'score', 'director', 'scriptwriter', 'actors', 'country', 'language',
                    'time', 'created_time', 'last_update_time', 'is_delete', 'contends')
    list_editable = ['is_delete']
