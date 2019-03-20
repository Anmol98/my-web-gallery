from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 80) #This is the charfield of our model, named title
    picture = models.ImageField(default='img/default.png', upload_to='img', blank=True, null=True) #This is used to add images
    description = models.TextField() #This is used to add unlimited text.
    published_date = models.DateTimeField(blank=True, null=True) #This is used to add date and times to our field

    def postit(self):
        self.published_date = timezone.now()
        self.save
    def __str__(self):
        return self.title
