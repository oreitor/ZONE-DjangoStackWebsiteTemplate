from django.db import models

# Create your models here.

class Message(models.Model):
    name = models.TextField(max_length=50)
    email = models.EmailField(max_length=70)
    text = models.TextField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name