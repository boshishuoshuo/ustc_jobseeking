from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Comments(models.Model):
    comment = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
