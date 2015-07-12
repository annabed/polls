from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model=Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fields=['pub_date', 'question_text']
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')


admin.site.register(Question,QuestionAdmin)

