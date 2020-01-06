from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id}: {self.name}'


class Question(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    hint = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    point = models.IntegerField()

    def __str__(self):
        return f'{self.name} [{self.point}]'


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} -> {self.question}'
