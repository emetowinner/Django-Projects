from django.db import models
from django.db.models.fields.files import ImageField

class UserCase(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='UseCase/')
    url = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title[0:20]+'...'

class UIProject(models.Model):
    image = models.ImageField(upload_to='UIProject/')
    title = models.CharField(max_length=100,default='N/A')
    description = models.CharField(max_length=400,default='N/A')
    url = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.url[0:20]+'...'

class PersonalData(models.Model):
    intro = models.CharField(max_length=400)
    about = models.TextField()
    image = models.ImageField(upload_to='Profile/')
    address = models.CharField(max_length=300,default='A108 Adam Street, New York, NY 535022')
    email = models.CharField(max_length=200,default='queeneomah@gmail.com')
    phone = models.CharField(max_length=15,default='+234-704 0787 822')

    def __str__(self) -> str:
        return self.intro[0:30]+'...'

class Assets(models.Model):
    favicon = models.CharField(max_length=1000)
    logo = models.CharField(max_length=1000)
    cv = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return 'Asset'