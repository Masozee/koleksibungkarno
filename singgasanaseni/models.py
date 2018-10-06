from django.db import models


# perupa --------------------------------------------------------------------------------------------
class perupa(models.Model):
    Nama = models.CharField(max_length=50)
    Panggilan = models.CharField(max_length=20, null=True, blank= True)
    Alamat = models.TextField(null=True, blank=True)
    Tempat_Lahir = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Lahir = models.DateField(null=True, blank=True)
    Tempat_Wafat = models.CharField(max_length=50, null=True, blank=True)
    Tanggal_Wafat = models.DateField(null=True, blank=True)
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

    No_Index = models.CharField(max_length=50)
    Judul = models.CharField(max_length=50)
    Perupa = models.ForeignKey(perupa, on_delete=models.CASCADE)
    Jenis = models.CharField(max_length=10, choices=KARYA_CHOICES)
    Dimensi = models.CharField(max_length=25)
    Material = models.CharField(max_length=20)
    Tahun_Pembuatan = models.DateField(blank=True, null=True)
    Gambar = models.FileField(upload_to='karya/', null=False)
    Lokasi_Lukisan = models.ForeignKey(istana, on_delete=models.CASCADE)
    Keterangan = models.TextField(null=True, blank=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Judul


class acara(models.Model):
    Nama = models.CharField(max_length=50)
    Lokasi = models.TextField()
    Mulai = models.DateTimeField()
    Akhir = models.DateTimeField()
    Keterangan = models.TextField(blank=True, null=True)
    Img = models.FileField(upload_to= 'acara/',blank=True, null=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nama

class kurator(models.Model):
    Nama = models.CharField(max_length=50)
    Alamat = models.TextField(null=True, blank=True)
    Tempat_Lahir = models.CharField(max_length=50)
    Tanggal_Lahir = models.DateField(null=True, blank=True)
    Keterangan = models.TextField(blank=True, null=True)
    Gambar = models.FileField(upload_to='kurator/', blank=True, null=True)
    Upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Nama