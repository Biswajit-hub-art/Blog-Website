from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','date']
    list_display_links = ['title','date']
    search_fields = ['title','content']
    list_filter = ['date']

admin.site.register(Post, PostAdmin)