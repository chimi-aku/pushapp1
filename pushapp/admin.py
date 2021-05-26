from django.contrib import admin
from django.conf.locale.es import formats as es_formats

es_formats.DATETIME_FORMAT = "d M Y H:i:s"
# Register your models here.

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'age',
    )
    fields = (
        'user',
        'age'
    )

admin.site.register(Person, PersonAdmin)




from .models import PushUps

class PushUpsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'numOfPushUps',
        'date',
    )
    list_editable = (
        'numOfPushUps',
    )
    list_filter = (
        'user',
        'date',
    )
    search_fields = ['user__user__username', ]
    fields = (
        'user',
        'numOfPushUps',
        'date',
    )

admin.site.register(PushUps, PushUpsAdmin)

