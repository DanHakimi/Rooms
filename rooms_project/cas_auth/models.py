from django.db import models


class CASUser(models.Model):
    username = models.CharField(max_length=255)
    is_admin = models.BooleanField()

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
        }

class UnauthenticatedUser(object):
    def __nonzero__(self):
        return False

    def is_authenticated(self):
        return False

    def get_and_delete_messages(self):
        return []