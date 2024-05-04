from django.contrib import admin
from .models import SumulaModel, TribNameSumulaModel, SiglaTribSumulaModel


class SumulaAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'enunciado']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = SumulaModel
        
class TribNameAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TribNameSumulaModel
        
class SiglaTribAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = SiglaTribSumulaModel

admin.site.register(SumulaModel, SumulaAdmin)
admin.site.register(TribNameSumulaModel, TribNameAdmin)
admin.site.register(SiglaTribSumulaModel, SiglaTribAdmin)