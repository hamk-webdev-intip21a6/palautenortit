from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'comment', 'date')
    list_filter = ['date']
    search_fields = ['comment']

admin.site.register(Post, PostAdmin)
