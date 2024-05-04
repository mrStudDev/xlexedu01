from django.contrib import admin
from .models import (
    DocumentsModel,
    RamoDireitoDocModel,
    TipoDocumentModel,
    TagDocumentsModel,
)

class ModeloAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'content_doc']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = DocumentsModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = RamoDireitoDocModel

class TipoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = TipoDocumentModel
        
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  

    class Meta:
        model = TagDocumentsModel

admin.site.register(DocumentsModel, ModeloAdmin)
admin.site.register(TipoDocumentModel, TipoAdmin)
admin.site.register(RamoDireitoDocModel, RamoAdmin)
admin.site.register(TagDocumentsModel, TagAdmin)