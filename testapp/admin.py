from django.contrib import admin
from testapp.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','body')
    raw_id_fields=('author',)
    list_filter=('status','author','publish','created')
    date_hierarchy = 'publish'
    ordering = ['status','publish']

class CommentAdmin(admin.ModelAdmin):
    list_display=('name','email','post','body','created','updated','active')
    list_filter=('active','created','updated')
    search_fields=('name','email','body')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
