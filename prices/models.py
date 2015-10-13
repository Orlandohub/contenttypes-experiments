from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class RentPriceTable(models.Model):
    number_days = models.IntegerField(_("Number of days"), default=0)
    price = models.DecimalField(_("Price per day"), max_digits=6, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = _("Rent price table")
        verbose_name_plural = _("Rent price tables")
        ordering = ('number_days', )

    def __str__(self):
        return "days: %s, price: %s" % (self.number_days, self.price)


class SellingPrice(models.Model):
    price = models.DecimalField(_('price'), max_digits=8, decimal_places=2, default=0, blank=True)
    old_price_sell = models.DecimalField(_('old price'), max_digits=8, decimal_places=2, default=None, null=True, blank=True)

    class Meta:
        verbose_name = _("Selling price")
        verbose_name_plural = _("Selling price")

    def __str__(self):
        return "price: %s" % self.price
