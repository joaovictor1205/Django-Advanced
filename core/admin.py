from django.contrib import admin
from core.models import *

class PersonAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')
    
admin.site.register(Person, PersonAdmin)
admin.site.register(Produto)
admin.site.register(Pedido)