from django.db import models


class Order(models.Model):
    account = models.ForeignKey('Account', blank=False, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=100, blank=True)
    items = models.TextField()
    order_time = models.DateTimeField(auto_now=True)
    price_paid = models.IntegerField(blank=False)
    price_ship = models.IntegerField(blank=False)
    price_items = models.IntegerField(blank=False)

    SHIPPING_STATUS_CHOICES = [
        ('U', 'unpaid'),
        ('P', 'preparing'),
        ('S', 'shipping'),
        ('A', 'arrived'),
        ('R', 'reviewed'),
    ]

    shipping_status = models.CharField(
        max_length=1,
        choices=SHIPPING_STATUS_CHOICES,
        default='U',
        blank=False
    )

    def __str__(self):
        return self.account.username.__str__() + self.order_time.__str__()

