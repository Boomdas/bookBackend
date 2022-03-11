import uuid
from django.db import models
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
# from django.urls import reverse


class BookAdmin(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length= 20)
    password = models.CharField(max_length = 20)