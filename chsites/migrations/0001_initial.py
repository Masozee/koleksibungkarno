# Generated by Django 2.1.5 on 2019-03-11 05:10

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Tittle', models.TextField()),
                ('SubTittle', models.TextField(blank=True, null=True)),
                ('Source', models.CharField(max_length=25)),
                ('Link', models.TextField()),
                ('Content', models.TextField()),
                ('Image', models.FileField(blank=True, upload_to='berita/')),
                ('Published', models.BooleanField(default=True)),
                ('Upload_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'News in Chinese',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
