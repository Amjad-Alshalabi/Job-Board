from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, related
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

def image_name(instance, filename):
    imagename , extention = filename.split('.')
    return "jobs/%s/%s.%s"%(instance.id, instance.id, extention.lower())

    


class Job(models.Model):
    owner = models.ForeignKey(User, on_delete=CASCADE)
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    experience = models.IntegerField(default=1)
    image = models.ImageField(upload_to =image_name, null = True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title

    
class apply(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now= True)
    

    def __str__(self):
        return self.name