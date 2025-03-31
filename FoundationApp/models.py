from django.db import models

# Create your models here.
class ImageModel(models.Model):
    memberimage = models.ImageField(upload_to='images/')
    membername = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.membername


class EventModel(models.Model):
    eventimage = models.ImageField(upload_to='events/')
    def __str__(self):
        return str(self.id)



class UserModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.email
