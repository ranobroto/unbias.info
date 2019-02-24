from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Articleupload(models.Model):
    title = models.TextField()
    text = models.TextField()
    postdate = models.DateField(default=timezone.now)
    imageurl = models.TextField()
    articleurl = models.TextField(default = "www.google.com")
    subreddit = models.CharField(max_length=50)
    votes = models.ManyToManyField('auth.User', related_name ='likes', blank=True)
    annotations_total = models.IntegerField()
    pscore = models.FloatField()
    biastext = models.TextField()
    biascolor = models.TextField()

class Comment(models.Model):
    post = models.ForeignKey('blog.Articleupload', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
