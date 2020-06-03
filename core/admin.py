from django.contrib import admin
from core.models import Person

class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')
    
admin.site.register(Person, PersonAdmin)