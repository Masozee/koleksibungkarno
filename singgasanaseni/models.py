from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse
import datetime

from django.db.models import Q

class PerupaQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(Nama__icontains=query) |
                         Q(Panggilan__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class PerupaManager(models.Manager):
    def get_queryset(self):
        return PerupaQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)



# perupa --------------------------------------------------------------------------------------------
class perupa(models.Model):
    PERUPA_CHOICES = (
        ('Pelukis', 'Pelukis'),
        ('Pematung', 'Pematung'),
        ('Pengrajin', 'Pengrajin'),
    )

    Nama = models.CharField(max_length=50)
    Panggilan = models.CharField(max_length=50, null=True, blank= True)
    Alamat = models.TextField(null=True, blank=True)
    Tempat_Lahir = models.CharField(max_length=50, blank=True)
    Tanggal_Lahir = models.CharField(max_length=50, blank=True)
    Tempat_Wafat = models.CharField(max_length=50, blank=True)
    Tanggal_Wafat = models.CharField(max_length=50, blank=True)
    Kategori = models.CharField(max_length=10, choices=PERUPA_CHOICES, default=True)
    Keterangan = models.TextField(null=True, blank=True, default="No detailed Information available")
    Description = models.TextField(null=True, blank=True, default="No detailed Information available")
    Sumber = models.CharField(max_length=50, blank=True )
    Link = models.TextField(blank=True, default="#")
    Gambar = models.FileField(upload_to='perupa/', blank=True, null=True)
    Upload_date = models.DateTimeField(auto_now_add=True)


    object  = PerupaManager()


    def __str__(self):
        return self.Panggilan

    def get_absolute_url(self):
        return reverse('perupa-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Perupa'





class KaryaQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(Judul__icontains=query)
                        )
            qs = qs.filter(or_lookup)# distinct() is often necessary with Q lookups
        return qs

class KaryaManager(models.Manager):
    def get_queryset(self):
        return KaryaQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

# Karya ----------------------------------------------------------------------------------------------
class karya(models.Model):
    ISTANA_CHOICES = (
        ('Istana Bogor', 'Istana Bogor'),
        ('Istana Tampak Siring', 'Istana Tampak Siring'),
        ('Istana Merdeka', 'Istana Merdeka'),
        ('Istana Negara', 'Istana Negara'),
        ('Istana Cipanas', 'Istana Cipanas'),
        ('palace Yogya', 'Istana Yogya')
    )

    KARYA_CHOICES = (
        ('Lukisan', 'Lukisan'),
        ('Patung', 'Patung'),
        ('Kriya', 'Kriya'),
    )
    KATEGORI_CHOICES = (
        ('Potret dan Sensualitas', 'Potret dan Sensualitas'),
        ('Alam dan Benda', 'Alam dan Benda'),
        ('Pemandangan Alam dan Kota', 'Pemandangan Alam dan Kota'),
        ('Perjuangan dan Potret Para Pejuang', 'Perjuangan dan Potret Para Pejuang'),
        ('Tradisi/Budaya/Mitologi/Keseharian', 'Tradisi/Budaya/Mitologi/Keseharian'),
        ('Patung dan Kriya', 'Patung dan Kriya'),
    )

    No_Index = models.CharField(max_length=50)
    Judul = models.CharField(max_length=100)
    Perupa = models.ForeignKey(perupa ,on_delete=models.CASCADE)
    Jenis = models.CharField(max_length=10, choices=KARYA_CHOICES,)
    Kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default=True)
    Dimensi = models.CharField(max_length=25)
    Material = models.CharField(max_length=20)
    Tahun_Pembuatan = models.DateField(blank=True, null=True)
    Gambar = models.FileField(upload_to='karya/', null=False)
    Lokasi_Lukisan = models.CharField(max_length=20, choices=ISTANA_CHOICES, default=True)
    Keterangan = models.TextField(null=True, blank=True)
    Naked_Material = models.BooleanField(default=False)
    Upload_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()


    object = KaryaManager()



    def __str__(self):
        return self.Judul

    def get_absolute_url(self):
        return reverse('karya-detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Karya'



class BeritaQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(Judul__icontains=query) |
                         Q(Subjudul__icontains=query) |
                         Q(Isiberita__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

class BeritaManager(models.Manager):
    def get_queryset(self):
        return BeritaQuerySet(self.model, using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

class berita(models.Model):
    Tanggal = models.DateField(blank=True, null=True)
    Judul = models.TextField(blank=True, null=True)
    Subjudul = models.TextField(blank=True, null=True)
    Sumber = models.CharField(max_length=50, blank=True, null=True)
    Link = models.TextField(blank=True, null=True)
    Isiberita = models.TextField()
    Gambar=models.FileField(upload_to='berita/', blank=True, null=True)
    Published=models.BooleanField(default=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    object=BeritaManager()

    def __str__(self):
        return self.Judul

    def get_absolute_url(self):
        return reverse('berita-list', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'Berita'


class HomeSlide(models.Model):
    tema = models.CharField(max_length=100,default=True)
    slide1 = models.FileField(upload_to='homepage/')
    caption1 = models.CharField(max_length=25, null=True, blank=True)
    subcaption1 = models.CharField(max_length=50, null=True, blank=True)
    link1=models.TextField(null=True, blank=True)
    slide2 = models.FileField(upload_to='homepage/')
    caption2 = models.CharField(max_length=25, null=True, blank=True)
    subcaption2 = models.CharField(max_length=50, null=True, blank=True)
    link2 = models.TextField(null=True, blank=True)
    slide3 = models.FileField(upload_to='homepage/')
    caption3 = models.CharField(max_length=25, null=True, blank=True)
    subcaption3 = models.CharField(max_length=50, null=True, blank=True)
    link3 = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.tema

    class Meta:
        verbose_name_plural = 'Slider'

class Inquiry(models.Model):
    Nama = models.CharField(max_length=50)
    Email = models.EmailField()
    Judul = models.CharField(max_length=50)
    Pertanyaan = models.TextField()
    Replied = models.BooleanField(default=False)

    def __str__(self):
        return self.Judul

    class Meta:
        verbose_name_plural = 'Inquiry'
