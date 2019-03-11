# Generated by Django 2.1.5 on 2019-03-10 06:31

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='berita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tanggal', models.DateField(blank=True, null=True)),
                ('Judul', models.TextField(blank=True, null=True)),
                ('Subjudul', models.TextField(blank=True, null=True)),
                ('Sumber', models.CharField(blank=True, max_length=50, null=True)),
                ('Link', models.TextField(blank=True, null=True)),
                ('Isiberita', models.TextField()),
                ('Gambar', models.FileField(blank=True, null=True, upload_to='berita/')),
                ('Published', models.BooleanField(default=True)),
                ('Upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='HomeSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(default=True, max_length=100)),
                ('slide1', models.FileField(upload_to='homepage/')),
                ('caption1', models.CharField(blank=True, max_length=25, null=True)),
                ('subcaption1', models.CharField(blank=True, max_length=50, null=True)),
                ('link1', models.TextField(blank=True, null=True)),
                ('slide2', models.FileField(upload_to='homepage/')),
                ('caption2', models.CharField(blank=True, max_length=25, null=True)),
                ('subcaption2', models.CharField(blank=True, max_length=50, null=True)),
                ('link2', models.TextField(blank=True, null=True)),
                ('slide3', models.FileField(upload_to='homepage/')),
                ('caption3', models.CharField(blank=True, max_length=25, null=True)),
                ('subcaption3', models.CharField(blank=True, max_length=50, null=True)),
                ('link3', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='karya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('No_Index', models.CharField(max_length=50)),
                ('Judul', models.CharField(max_length=100)),
                ('Jenis', models.CharField(choices=[('Lukisan', 'Lukisan'), ('Patung', 'Patung'), ('Kriya', 'Kriya')], max_length=10)),
                ('Kategori', models.CharField(choices=[('Potret dan Sensualitas', 'Potret dan Sensualitas'), ('Alam dan Benda', 'Alam dan Benda'), ('Pemandangan Alam dan Kota', 'Pemandangan Alam dan Kota'), ('Perjuangan dan Potret Para Pejuang', 'Perjuangan dan Potret Para Pejuang'), ('Tradisi/Budaya/Mitologi/Keseharian', 'Tradisi/Budaya/Mitologi/Keseharian'), ('Patung dan Kriya', 'Patung dan Kriya')], default=True, max_length=50)),
                ('Dimensi', models.CharField(max_length=25)),
                ('Material', models.CharField(max_length=20)),
                ('Tahun_Pembuatan', models.DateField(blank=True, null=True)),
                ('Gambar', models.FileField(upload_to='karya/')),
                ('Lokasi_Lukisan', models.CharField(choices=[('Istana Bogor', 'Istana Bogor'), ('Istana Tampak Siring', 'Istana Tampak Siring'), ('Istana Merdeka', 'Istana Merdeka'), ('Istana Negara', 'Istana Negara'), ('Istana Cipanas', 'Istana Cipanas'), ('palace Yogya', 'Istana Yogya')], default=True, max_length=20)),
                ('Keterangan', models.TextField(blank=True, null=True)),
                ('Naked_Material', models.BooleanField(default=False)),
                ('Upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='perupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nama', models.CharField(max_length=50)),
                ('Panggilan', models.CharField(blank=True, max_length=50, null=True)),
                ('Alamat', models.TextField(blank=True, null=True)),
                ('Tempat_Lahir', models.CharField(blank=True, max_length=50)),
                ('Tanggal_Lahir', models.CharField(blank=True, max_length=50)),
                ('Tempat_Wafat', models.CharField(blank=True, max_length=50)),
                ('Tanggal_Wafat', models.CharField(blank=True, max_length=50)),
                ('Kategori', models.CharField(choices=[('Pelukis', 'Pelukis'), ('Pematung', 'Pematung'), ('Pengrajin', 'Pengrajin')], default=True, max_length=10)),
                ('Keterangan', models.TextField(blank=True, default='No detailed Information available', null=True)),
                ('Description', models.TextField(blank=True, default='No detailed Information available', null=True)),
                ('Gambar', models.FileField(blank=True, null=True, upload_to='perupa/')),
                ('Upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='karya',
            name='Perupa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='singgasanaseni.perupa'),
        ),
        migrations.AddField(
            model_name='karya',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
