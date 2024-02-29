from django.db import models

# Create your models here.
class ArticleModel(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    topic = models.CharField(max_length=40)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.title
    
class ContactModel(models.Model):

    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=100)
    gender = models.CharField(max_length=1)

    def __str__(self):
        return self.name