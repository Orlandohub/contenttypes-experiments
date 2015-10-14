from django.db import models
from django.utils.translation import ugettext_lazy as _
# from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from products.models import Product


# Create your models here.
class RentPriceTable(models.Model):
    number_days = models.IntegerField(_("Number of days"), default=0)
    price = models.DecimalField(_("Price per day"), max_digits=6, decimal_places=2, default=0.00)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _("Rent price table")
        verbose_name_plural = _("Rent price tables")
        ordering = ('number_days', )

    def __str__(self):
        return "days: %s, price: %s" % (self.number_days, self.price)


class SellingPrice(models.Model):
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2, default=0, blank=True)
    old_price_sell = models.DecimalField(_('old price'), max_digits=8, decimal_places=2, default=None, null=True, blank=True)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


    class Meta:
        verbose_name = _("Selling price")
        verbose_name_plural = _("Selling price")

    def __str__(self):
        return "price: %s" % self.price
