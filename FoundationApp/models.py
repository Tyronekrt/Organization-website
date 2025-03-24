from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class EventModel(models.Model):
    image = models.ImageField(upload_to='events/')
    def __str__(self):
        return str(self.id)
