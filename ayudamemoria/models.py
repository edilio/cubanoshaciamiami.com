from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class MemoryPhrase_Answer(models.Model):
    category = models.ForeignKey(Category)
    phrase = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.phrase

