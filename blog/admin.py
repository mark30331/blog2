from django.contrib import admin
#import the models you want the admin page to use
from .models import Post
from .models import Comment


# Register your models here.
@admin.register(Post)
# this decorator performs the same function as admin.site.register(Post)
class PostAdmin(admin.ModelAdmin): # customization of admin panel
    # display which columns of the database to appear on admin panel
    list_display = ['title', 'slug', 'author','publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug':('title',)}
    # raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    show_facets = admin.ShowFacets.ALWAYS # this shows the count of the columns 


    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email', 'post','created', 'active']
    list_filter = ['active', 'created','updated']
    search_fields = ['name', 'email', 'body']