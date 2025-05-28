from django.apps import AppConfig

#this includes the main configuration of the blog application
#provides the metadata about the blog application
class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
