from django.contrib import admin

from .models import (
    PrincipiosModel,
    RamoDireitoModel
)

class PrincipioAdmin(admin.ModelAdmin):
    list_display = ('principio_name', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['principio_name', 'meta_title', 'content_principio']
    prepopulated_fields = {"slug": ("principio_name",)}
    
    class Meta:
        model = PrincipiosModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = RamoDireitoModel

admin.site.register(PrincipiosModel, PrincipioAdmin)
admin.site.register(RamoDireitoModel, RamoAdmin)