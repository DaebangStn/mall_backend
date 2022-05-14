from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False)
    slug = models.SlugField(max_length=50, blank=False)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)

    def __str__(self):
        path = [self.name]
        p = self.parent
        while p is not None:
            path.append(p.name)
            p = p.parent
        return ' / '.join(path[::-1])
