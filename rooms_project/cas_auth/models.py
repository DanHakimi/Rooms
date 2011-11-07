from django.db import models


class CASUser(models.Model):
    username = models.CharField(max_length=255)
