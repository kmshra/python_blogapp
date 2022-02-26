from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True,null=True)
    # content = models.TextField()
    author = models.CharField(max_length=50)
    slug = models.CharField(max_length=150)
    blogimage = models.ImageField(upload_to='blog_image')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author