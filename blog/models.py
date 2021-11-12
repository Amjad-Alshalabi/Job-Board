from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

class comment(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    
    

    def __str__(self):
        return self.comment

    
class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name


class blog(models.Model):
    owner = models.ForeignKey(User , related_name='blog_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post = models.TextField(max_length=10000)
    comments = models.ForeignKey(comment, on_delete=models.CASCADE, blank=True, null=True)
    published_at = models.DateTimeField(auto_now= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(blog, self).save(*args, **kwargs)
    

    def get_date(self):
        time = datetime.now()
        if self.published_at.day == time.day:
            return str(time.hour - self.published_at.hour) + " hours ago"
        else:
            if self.published_at.month == time.month:
                return str(time.day - self.published_at.day) + " days ago"
            else:
                if self.published_at.year == time.year:
                    return str(time.month - self.published_at.month) + " months ago"
        return self.published_at

    def __str__(self):
        return self.title

    

