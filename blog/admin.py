from django.contrib import admin

# Register your models here.

from .models import Post,Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)} # new

admin.site.register(Post,BlogAdmin)
admin.site.register(Comment)
