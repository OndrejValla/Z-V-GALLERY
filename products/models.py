from django.db import models


class Project(models.Model):
    friendly_name = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    

    def __str__(self):
        return self.friendly_name


    def get_name(self):
        return self.name


class Product(models.Model):
    project = models.ForeignKey(
        'Project', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
