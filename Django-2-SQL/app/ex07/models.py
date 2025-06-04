from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(unique=True, max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=False)
    producer = models.CharField(max_length=128, null=False)
    release_date = models.DateField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    # Format the created datetime to show only hours, minutes, seconds
    @property
    def formatted_created(self):
        return self.created.strftime('%H:%M:%S')
    
    # Format the updated datetime to show only hours, minutes, seconds
    @property
    def formatted_updated(self):
        return self.updated.strftime('%H:%M:%S')