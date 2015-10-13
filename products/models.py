from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=120)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return u"%s" % self.name
