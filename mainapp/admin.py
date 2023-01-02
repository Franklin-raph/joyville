from django.contrib import admin
from .models import Blog,Newsletter

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	list_display=['author','title','date_posted',]
	prepopulated_fields= {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Newsletter)