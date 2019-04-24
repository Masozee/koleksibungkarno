from django.db import models


from django.db.models import Q
from singgasanaseni.models import karya



class NewsQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(Tittle__icontains=query) |
                         Q(SubTittle__icontains=query) |
                         Q(Content__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class NewsManager(models.Manager):
    def get_queryset(self):
        return NewsQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class News(models.Model):
    Date = models.DateField()
    Tittle = models.TextField()
    SubTittle = models.TextField(blank=True, null=True)
    Source = models.CharField(max_length=25)
    Link = models.TextField()
    Content = models.TextField()
    Image=models.FileField(upload_to='berita/', blank=True)
    Published=models.BooleanField(default=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    object=NewsManager()

    def __str__(self):
        return self.Tittle

    class Meta:
        verbose_name_plural = 'News in Chinese'


