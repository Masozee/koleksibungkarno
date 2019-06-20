# Generated by Django 2.2 on 2019-06-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singgasanaseni', '0004_privacy_tos'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pertanyaan', models.CharField(max_length=150)),
                ('Jawaban', models.TextField()),
                ('Pertanyaan_en', models.CharField(max_length=150)),
                ('Jawaban_en', models.TextField()),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Edited', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'FAQ',
            },
        ),
    ]
