from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=255)
