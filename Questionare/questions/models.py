from django.db import models

# Create your models here.

class Question(models.Model):
    title=models.TextField()
    name=models.TextField()

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    name=models.TextField()