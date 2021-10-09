from django.db import models


class Users(models.Model):
    firstname = models.CharField(max_length=128)
    secondname = models.CharField(max_length=128)
    user_login = models.CharField(max_length=64)
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.user_login


class Tasks(models.Model):
    title = models.CharField(max_length=128)
    name = models.CharField(max_length=256)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('Users', related_name='tasks', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
