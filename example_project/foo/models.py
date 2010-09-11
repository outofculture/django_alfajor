from django.db import models

class Foo(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    checked = models.BooleanField(default=True, blank=True)
