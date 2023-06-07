from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField 
from django.utils.text import slugify
from imagekit.processors import ResizeToFill
from ckeditor_uploader.fields import RichTextUploadingField
import re


# Create your models here.
class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name") # verbose_name is the name that will be displayed in the admin panel
    slug = models.SlugField(max_length=100, verbose_name="Slug") # slug is the name that will be displayed in the url
    
    @property
    def get_number_of_posts(self):
        return BlogPost.objects.filter(category=self).count()
    
    @property
    def get_absolute_url(self):
        return f"/category/{self.slug}/"
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
        ordering = ['id']


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    thumbnail = ProcessedImageField(upload_to='blog/thumbnails/%Y/%m/%d/', processors=[ResizeToFill(550,550)], format='PNG', options={'quality': 95}, verbose_name='Thumbnail', null=True)
    content = RichTextUploadingField(blank=True, null=True, verbose_name='Content');
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Category", db_index=True) 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    truncated_title = models.CharField(max_length=100, verbose_name="Truncated Title", null=True, blank=True)
    truncated_content = models.TextField(verbose_name="Truncated Content", null=True, blank=True)

    #overload save method to create truncated title and content
    def save(self, *args, **kwargs):
        max_content_length = 200
        max_title_length = 25
        formatted_content = re.sub('<.*?>|&nbsp;', '', self.content)

        if len(formatted_content) <= max_content_length: # if the content is less than or equal to 200 characters, then don't truncate it
            self.truncated_content = formatted_content # set the truncated content to the formatted content
        else:
            truncated_parts = [formatted_content[:max_content_length], "..."] # if the content is more than 200 characters, then truncate it
            self.truncated_content = "".join(truncated_parts) # join the truncated parts together to form the truncated content

        if len(self.title) <= max_title_length: # if the title is less than or equal to 25 characters, then don't truncate it
            self.truncated_title = self.title # set the truncated title to the title
        else:
            truncated_parts = [self.title[:max_title_length], "..."] # if the title is more than 25 characters, then truncate it
            self.truncated_title = "".join(truncated_parts) # join the truncated parts together to form the truncated title
         
        super().save(*args, **kwargs)
        
    
    @property
    def get_month_created(self): # this is a property that returns the month that the blog post was created
        return self.created_at.strftime("%b") # strftime is a function that formats a datetime object into a string
 
    @property
    def get_day_created(self): # this is a property that returns the day that the blog post was created
        return self.created_at.strftime("%d") 



    def __str__(self):
        return self.title # this is the name that will be displayed in the admin panel
    
    class Meta:
        verbose_name = "Blog Post" # this is the name that will be displayed in the admin panel
        verbose_name_plural = "Blog Posts" # this is the name that will be displayed in the admin panel of plural objects
        ordering = ['id'] # this is the order that the objects will be displayed in the admin panel

    

    

