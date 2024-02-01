from django.db import models


# Create your models here.
class AndroidApp(models.Model):
    name = models.CharField(max_length=50)
    points = models.CharField(max_length=20)
    # image = models.ImageField()
    url = models.CharField(max_length=100)

    @property
    def get_total_points(self):
        return self.points
