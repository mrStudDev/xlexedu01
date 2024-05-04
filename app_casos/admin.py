from django.contrib import admin

from .models import (
    CasoConcretoModel,
    DisciplinaCasosModel,
    RamoDireitoModel,
    TagCasoModel
    )

class CasosAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'pergunta_caso']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = CasoConcretoModel

class DisciplinaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = DisciplinaCasosModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = RamoDireitoModel

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)} 

    class Meta:
        model = TagCasoModel

admin.site.register(CasoConcretoModel, CasosAdmin)
admin.site.register(DisciplinaCasosModel, DisciplinaAdmin)
admin.site.register(RamoDireitoModel, RamoAdmin)
admin.site.register(TagCasoModel, TagAdmin)
