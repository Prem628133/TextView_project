from django.db import models

# Create your models here.
class text(models.Model):
    heading = models.CharField(max_length=20)
    paragraph = models.TextField(max_length=300)


    def __str__(self):
        return self.name

