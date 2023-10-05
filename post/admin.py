from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'address',
                    'date', 'author', 'updated_on', 'created_on', 'is_active', )

    list_filter = ('date',  'author','created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
