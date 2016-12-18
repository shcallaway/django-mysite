from django.contrib import admin
from .models import Question, Choice

# Allows us to add choice objects within a question object form
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # Display question choices inline
    inlines = [ChoiceInline]
    # Display question_text, pub_date, was_published_recently columns
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Add a filter on pub_date
    list_filter = ['pub_date']
    # Adds a search feature
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
