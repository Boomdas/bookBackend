import uuid
from django.db import models


class author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.TextField(max_length=600)

class bookmanage(models.Model):
    bookid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    bookname = models.CharField(max_length=50)
    bookimage = models.CharField(max_length=1000)
    bookgenary = models.CharField(max_length=50)
    authorid = models.ForeignKey(author, on_delete=models.CASCADE)
    bookdescription = models.TextField(max_length=600)
    bookratingid = models.CharField(max_length=150)
    bookpdf = models.FileField(max_length=20)
    dateofadd = models.CharField(max_length=50)

    def __str__(self):
        return ('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}').format(self.bookid, self.bookname, self.bookimage, self.bookgenary, self.authorid, self.bookdescription, self.bookratingid, self.bookpdf, self.dateofadd)




    def __str__(self):
        return ('{0}, {1}, {2}, {3}').format(self.id, self.name, self.image, self.description)
