from django.contrib import admin
from .models import HomeSite, TagSiteModel, ContactMessagesModel

class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title']
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        models = HomeSite
        
class TagSiteAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TagSiteModel
    
class ContactAdmin(admin.ModelAdmin):
    class Meta:
        model = ContactMessagesModel


admin.site.register(HomeSite, SiteAdmin)
admin.site.register(TagSiteModel, TagSiteAdmin)

