from django.db import models


# perupa --------------------------------------------------------------------------------------------
class perupa(models.Model):
    PERUPA_CHOICES = (
        ('Pelukis', 'Pelukis'),
        ('Pematung', 'Pematung'),
        ('Pengrajin', 'Pengrajin'),
    )

    Nama = models.CharField(max_length=50)
    Panggilan = models.CharField(max_length=20, null=True, blank= True)
    Alamat = models.TextField(null=True, blank=True)
    Tempat_Lahir = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Lahir = models.DateField(null=True, blank=True)
    Tempat_Wafat = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Wafat = models.DateField(null=True, blank=True)
    Kategori = models.CharField(max_length=10, choices=PERUPA_CHOICES, default=True)
    Keterangan = models.TextField(null=True, blank=True)
    Gambar = models.FileField(upload_to='perupa/', blank=True, null=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Panggilan


# istana ----------------------------------------------------------------------------------------------
class istana(models.Model):
    Nama = models.CharField(max_length=50)
    Alamat = models.TextField(null=True, blank=True)
    Gambar = models.FileField(upload_to='istana/', null=True)
    Keterangan = models.TextField(null=True, blank=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nama


# Karya ----------------------------------------------------------------------------------------------
class karya(models.Model):
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
    Lokasi_Lukisan = models.ForeignKey(istana, on_delete=models.CASCADE)
    Keterangan = models.TextField(null=True, blank=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Judul


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

    def __str__(self):
        return self.Judul

