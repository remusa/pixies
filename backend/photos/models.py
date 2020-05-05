import uuid

from django.db import models


class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    url = models.CharField(max_length=280)
    caption = models.CharField(max_length=280)
    details = models.CharField(max_length=280)

    def __str__(self):
        return self.caption
