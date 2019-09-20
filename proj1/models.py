from django.db import models

# Create your models here.

class Home_Page(models.Model):
    title = models.CharField(max_length=60)
    bodytext = models.TextField('Page Content', blank=True)
    created = models.DateTimeField()

    def __str__(self):
        return self.title
