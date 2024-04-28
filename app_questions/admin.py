from django.contrib import admin

from .models import (
    XlexQuestionModel,
    DisciplinaQuestionModel,
    BancaQuestionModel,
    RamoDireitoQuestionModel,
    TagQuestionModel,
    AlternativasModel
    )

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('date_created', 'indexable', '__str__')  # Adiciona indexable e mantém __str__
    list_editable = ('indexable',)  # Permite que indexable seja editável diretamente na lista
    list_filter = ('indexable',)  # Adiciona indexable aos filtros
    list_filter = ["date_created"]
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = XlexQuestionModel

class DisciplinaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = DisciplinaQuestionModel

class BancaAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = BancaQuestionModel

class RamoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = RamoDireitoQuestionModel

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    class Meta:
        model = TagQuestionModel


admin.site.register(XlexQuestionModel, QuestionAdmin)
admin.site.register(DisciplinaQuestionModel, DisciplinaAdmin)
admin.site.register(BancaQuestionModel, BancaAdmin)
admin.site.register(RamoDireitoQuestionModel, RamoAdmin)
admin.site.register(TagQuestionModel, TagAdmin)
admin.site.register(AlternativasModel)