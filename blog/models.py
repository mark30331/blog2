from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from taggit.managers import TaggableManager

#creation of custom query set (default is 'objects')
class PublishedManager(models.Manager):
    # custom queryset to retrieve published posts
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    

# Create your models here.
#  models inherits from the base Model class
class Post(models.Model):
    # creation of custom choices to be used in the database
    class Status(models.TextChoices):
        DRAFT = 'DF' , 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=Status,default=Status.DRAFT)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='blog_posts')

    objects = models.Manager()
    published = PublishedManager()

    #tags manager will allow you to add, retrieve, and remove 
    # tags from posts objects
    tags = TaggableManager()


    class Meta: # this defines the meta data of the table
        # ordering attribute to tell django that it should 
        # sort results by the publish field in decending order
        # by using the hyphen before the field name
        ordering = ['-publish']
        # stores pointers to the data in databases for faster lookups
        indexes = [models.Index(fields=['-publish'])]

    def __str__(self):
        return self.title
    
    # using the reverse function to build canonical urls for 
    # search engines and seo
    # The reverse() function will build the URL dynamically
    # using the URL name defined in the URL patterns.
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[
                            self.publish.year, 
                            self.publish.month,
                            self.publish.day,
                            self.slug])
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering= ['created']
        indexes = [models.Index(fields=['created']),]
    
    def __str__(self):
        return f'comment by {self.name} on {self.post}'
    