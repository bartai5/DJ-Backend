from django.db import models

class UserList(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    post=models.TextField()


    def __str__(self):
        return self.name