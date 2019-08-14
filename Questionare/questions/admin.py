from django.contrib import admin

# Register your models here.
from .models import Question,Choice
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['type']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)