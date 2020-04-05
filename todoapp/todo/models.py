from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    date_create = models.DateField(auto_now_add=True)
