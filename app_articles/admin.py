from django.contrib import admin

from .models import (
    CategoryArticlesModel,
    TagArticlesModel,
    ArticlesModel,
    )


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'meta_title', 'date_created', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'content']
    prepopulated_fields = {"slug": ("title",)}
    
    class Meta:
        model = ArticlesModel

       
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = CategoryArticlesModel

                                            
class TagArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    class Meta:
        model = TagArticlesModel
    

admin.site.register(ArticlesModel, ArticleAdmin)
admin.site.register(CategoryArticlesModel, CategoryAdmin)
admin.site.register(TagArticlesModel, TagArticleAdmin)
