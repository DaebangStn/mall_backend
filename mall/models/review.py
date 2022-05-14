from django.db import models


class Review(models.Model):
    order = models.OneToOneField('Order', on_delete=models.CASCADE)
    reviewed_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=50, blank=False)
    text = models.TextField()
