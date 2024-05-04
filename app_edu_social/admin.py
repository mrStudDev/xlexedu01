from django.contrib import admin

from .models import (
    ArticlesSocialModel,
    CategorySocialModel,
    TagSocialModel
    )


class ArticleSocialAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'content_social']
    prepopulated_fields = {"slug": ("title",)}
    
    
    class Meta:
        model = ArticlesSocialModel

       
class CategorySocialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = CategorySocialModel

                                            
class TagArticleSocialAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TagSocialModel
    

admin.site.register(ArticlesSocialModel, ArticleSocialAdmin)
admin.site.register(CategorySocialModel, CategorySocialAdmin)
admin.site.register(TagSocialModel, TagArticleSocialAdmin)
