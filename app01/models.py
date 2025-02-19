from django.db import models
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)
    like = models.IntegerField(default=0)
    #image = models.ImageField(upload_to='images',null=True, blank=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField()
    posted_at = models.DateTimeField(default=timezone.now)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
