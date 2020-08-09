from django.db import models


# Create your models here.
class Flower(models.Model):
    title = models.CharField(default="", max_length=50)
    description = models.TextField(default='')
    datepick = models.DateField(auto_now=False)
    image = models.ImageField(default='', upload_to='images')

    def __str__(self):
        return self.title


class SelChoice(models.Model):
    titleSelect = models.ForeignKey(Flower,on_delete=models.CASCADE)

    def __str__(self):
        return self.titleSelect
