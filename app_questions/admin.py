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
    list_display = ('title', 'meta_title', 'is_published', 'indexable')
    list_editable = ('meta_title', 'is_published', 'indexable')
    list_filter = ('indexable', 'date_created')  # Combina ambos os filtros em uma única declaração
    search_fields = ['title', 'meta_title', 'question_ask']
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