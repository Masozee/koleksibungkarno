from django.db import models


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
    Tempat_Lahir = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Lahir = models.DateField(null=True, blank=True)
    Tempat_Wafat = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Wafat = models.DateField(null=True, blank=True)
    Kategori = models.CharField(max_length=10, choices=PERUPA_CHOICES, default=True)
    Keterangan = models.TextField(null=True, blank=True)
    Gambar = models.FileField(upload_to='perupa/', blank=True, null=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    object  = PerupaManager()


    def __str__(self):
        return self.Panggilan



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
        ('istana Yogya', 'Istana Yogya')
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

    No_Index = models.CharField(max_length=50, unique=True)
    Judul = models.CharField(max_length=50)
    Perupa = models.ForeignKey(perupa ,on_delete=models.CASCADE)
    Jenis = models.CharField(max_length=10, choices=KARYA_CHOICES,)
    Kategori = models.CharField(max_length=50, choices=KATEGORI_CHOICES, default=True)
    Dimensi = models.CharField(max_length=25)
    Material = models.CharField(max_length=20)
    Tahun_Pembuatan = models.DateField(blank=True, null=True)
    Gambar = models.FileField(upload_to='karya/', null=False)
    Lokasi_Lukisan = models.CharField(max_length=20, choices=ISTANA_CHOICES, default=True)
    Keterangan = models.TextField(null=True, blank=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    object = KaryaManager()



    def __str__(self):
        return self.Judul


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
    Tanggal = models.DateField()
    Judul = models.TextField()
    Subjudul = models.TextField(blank=True, null=True)
    Sumber = models.CharField(max_length=10)
    Link = models.TextField()
    Isiberita = models.TextField()
    Gambar=models.FileField(upload_to='berita/', blank=True)
    Published=models.BooleanField(default=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    object=BeritaManager()




    def __str__(self):
        return self.Judul

