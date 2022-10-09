from django.db import models
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='.imgs/default -image.jpg')
    image_link = models.URLField(max_length=150, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Certificate(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='Upload', null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name
    def imageURL(self):
        try:
            return self.image.url
        except:
            pass

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    number = models.CharField(max_length=30, blank=True, null=True)
    subject = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

class Resume(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    file = models.FileField()
    def __str__(self):
        return self.name
