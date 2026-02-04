from django.db import models
from django.core.validators import MinValueValidator

# Product model
class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField()
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    amount = models.IntegerField(default=0, null=False, validators=[MinValueValidator(0)])

    @property
    def in_stock():
        return self.amout > 0

    def __str__():
        return self.name