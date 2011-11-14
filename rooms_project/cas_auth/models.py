from django.db import models


class CASUser(models.Model):
    username = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
        }