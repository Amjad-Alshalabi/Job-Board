from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.


JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

class Category(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now= True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    experience = models.IntegerField(default=1)
    

    def __str__(self):
        return self.title