import uuid
from django.db import models
# from django.template.defaultfilters import slugify
# from django.contrib.auth.models import User
# from django.urls import reverse


class BookAdmin(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length= 20)
    password = models.CharField(max_length = 20)
    # def __init__(self, name, password):
    #     self.name = name
    #     self.password = password
        
    def __str__(self):
        return ('{0}, {1}, {2}').format(self.id, self.name, self.password)