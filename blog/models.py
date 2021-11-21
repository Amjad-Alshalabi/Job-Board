from django.db import models
from django.db.models.fields.related import ForeignKey, OneToOneField
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.text import slugify
import random
import string
import time
# Create your models here.






class Post(models.Model):
    owner = models.ForeignKey(User , related_name='post_user', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
  
    published_at = models.DateTimeField(auto_now= True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    

    
    def save(self, *args, **kwargs):
        self.slug = self.generate_slug()
        return super(Post, self).save(*args, **kwargs)

    def generate_slug(self, save_to_obj=False, add_random_suffix=True):
        """
        Generates and returns slug for this obj.
        If `save_to_obj` is True, then saves to current obj.
        Warning: setting `save_to_obj` to True
              when called from `.save()` method
              can lead to recursion error!

        `add_random_suffix ` is to make sure that slug field has unique value.
        """

        # We rely on django's slugify function here. But if
        # it is not sufficient for you needs, you can implement
        # you own way of generating slugs.
        generated_slug = slugify(self.title)

        # Generate random suffix here.
        random_suffix = ""
        if add_random_suffix:
            random_suffix = ''.join([
                random.choice(string.ascii_letters + string.digits)
                for i in range(5)
            ])
            generated_slug += '-%s' % random_suffix

        if save_to_obj:
            self.slug = generated_slug
            self.save(update_fields=['slug'])
        
        return generated_slug
    
    def get_date(self):
        time = datetime.now()
        # time = datetime.now().time()
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

    



class Comments(models.Model):
    owner = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='details', on_delete=models.CASCADE)
    comment  = models.TextField()
    comment_date  = models.DateTimeField(auto_now= True)
    class Meta:
        ordering = ('-comment_date',)
    

    def __str__(self):
        return 'Comment by {}'.format(self.owner)