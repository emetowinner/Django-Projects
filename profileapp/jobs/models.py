from django.db import models

class Job(models.Model):
    image = models.ImageField(default = 'CSAM.png', upload_to='images/')
    summary = models.TextField()
    view_count = models.IntegerField(default=0)
