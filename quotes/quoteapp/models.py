from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100, null=False, unique=True)
    born_date = models.CharField(null=False)
    born_location = models.CharField(max_length=150, null=False)
    description = models.TextField(null=False)

    def __str__(self):
        return f"{self.fullname}"

class Quote(models.Model):
    quote = models.CharField(null=False)
    tags = models.ManyToManyField(Tag)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"{self.quote}"
