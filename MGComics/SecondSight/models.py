from django.db import models
from django.utils import timezone


STATUS = (
    ('s', "Show"),
    ('', "Hide"),
    ('d', 'DELETE')
)


# News blog model 
class Newspost(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, default='')
    title = models.CharField(max_length=50)
    group_id = models.CharField(max_length=50)
    text = models.TextField(max_length=5000)
    created_date = models.DateTimeField(default=timezone.now)
    manage = models.CharField(max_length=10, choices=STATUS, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


# About model
class User(models.Model):
    name = models.CharField(max_length=25, blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, default='')
    description = models.TextField(max_length=900, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


# Sticky model
class Sticky(models.Model):
    name = models.CharField(max_length=25, blank=True, default='')
    image = models.ImageField(upload_to='images/', blank=True, default='')
    description = models.TextField(max_length=900, blank=True, default='')
    status = models.CharField(max_length=50, blank=True, default='')
    date = models.CharField(max_length=50, blank=True, default='')
    manage = models.CharField(max_length=10, choices=STATUS, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Chapter(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title


# Comic model
class Comic(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    group_id = models.CharField(max_length=50, blank=True, default='')
    description = models.CharField(max_length=500, blank=True, default='')
    transcript = models.CharField(max_length=500, blank=True, default='')

    def __str__(self):
        return self.title

# Gallery Model
class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=500, blank=True, default='')
    manage = models.CharField(max_length=10, choices=STATUS, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

# cover banner
class CoverBanner(models.Model):
    title = models.CharField(max_length=50, blank=True, default='')
    image = models.ImageField(upload_to='images/')
    tag_line = models.CharField(max_length=900, blank=True, default='')
    description = models.CharField(max_length=900, blank=True, default='')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title
