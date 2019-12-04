# Generated by Django 2.2 on 2019-06-19 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singgasanaseni', '0003_auto_20190609_1322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Privacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=150)),
                ('Isi', models.TextField()),
                ('Judul_en', models.CharField(max_length=150)),
                ('Isi_en', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Privacy Policy',
            },
        ),
        migrations.CreateModel(
            name='Tos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Judul', models.CharField(max_length=150)),
                ('Isi', models.TextField()),
                ('Judul_en', models.CharField(max_length=150)),
                ('Isi_en', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Term of Services',
            },
        ),
    ]