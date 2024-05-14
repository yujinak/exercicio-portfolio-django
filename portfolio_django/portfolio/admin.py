from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status')
    search_fields = ['title', 'author', 'content']
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Post, PostAdmin)