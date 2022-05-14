from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)
    slug = models.SlugField(max_length=50, blank=False, unique=True)
    price = models.IntegerField(blank=False)
    detail_link = models.CharField(max_length=100, blank=True)
    options = models.TextField(blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_cat_list(self):
        c = self.category
        breadcrumb = ['dummy']
        while c is not None:
            breadcrumb.append(c.slug)
            c = c.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])

        return breadcrumb[-1:0:-1]
