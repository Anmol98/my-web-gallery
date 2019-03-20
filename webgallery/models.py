from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length = 80)
    picture = models.ImageField(default='img/default.png', upload_to='img', blank=True, null=True)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def postit(self):
        self.published_date = timezone.now()
        self.save
    def __str__(self):
        return self.title
