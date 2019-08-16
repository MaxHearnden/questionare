from django.db import models

# Create your models here.

class Page(models.Model):
    title=models.TextField()
    submitAddr=models.TextField(default="/submit")
    def __str__(self):
        return self.title

class Question(models.Model):
    title=models.TextField()
    name=models.TextField()
    type=models.TextField(default="radio")
    order=models.IntegerField(default=1)
    page=models.ForeignKey(Page,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.title

class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    name=models.TextField()
    def __str__(self):
        return self.name+" for "+self.question.title

class Response(models.Model):
    date_done=models.DateTimeField('date sent')
    def __str__(self):
        return "response"

class Answer(models.Model):
    response=models.ForeignKey(Response,on_delete=models.CASCADE)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    answer=models.TextField()
    def __str__(self):
        return self.answer+" for "+self.question.title