# Generated by Django 2.1.5 on 2019-01-31 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tittle', models.TextField()),
                ('SubTittle', models.TextField(blank=True, null=True)),
                ('Source', models.CharField(max_length=10)),
                ('Link', models.TextField()),
                ('Content', models.TextField()),
                ('Gambar', models.FileField(blank=True, upload_to='news/')),
                ('Published', models.BooleanField(default=True)),
                ('Upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
