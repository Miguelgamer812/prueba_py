from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="images", blank=True)#blank true me crea el campo nulo en la tabla

    def __str__(self):
        return self.title