from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    message = models.TextField(max_length=250, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
