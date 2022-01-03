from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField

from profiles.models import UserProfile
from products.models import Product


class Review(models.Model):
    class Meta:
        ordering = ['-id']

    RATING = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=254, null=False, blank=False)
    comment = models.TextField(max_length=1500, null=False, blank=False)
    rating = models.IntegerField(choices=RATING, null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
