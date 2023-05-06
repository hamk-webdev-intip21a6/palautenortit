from django.contrib import admin
from .models import Topic, Feedback
from django.db.models import Avg

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_average_rating')
    search_fields = ['name']

    def display_average_rating(self, obj):
        average_rating = Feedback.objects.filter(topic=obj).aggregate(Avg('rating'))['rating__avg']
        return f"{average_rating:.2f}" if average_rating else "N/A"
    display_average_rating.short_description = 'Keskiarvo'

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('topic', 'rating', 'good', 'bad', 'ideas', 'date')
    list_filter = ['topic', 'date']
    search_fields = ['good', 'bad', 'ideas',]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Feedback, FeedbackAdmin)

