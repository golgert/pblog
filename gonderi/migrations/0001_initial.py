# Generated by Django 2.0.2 on 2018-03-05 20:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ileti',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=60)),
                ('baslik', models.CharField(max_length=80)),
                ('yazi_tarihi', models.DateField()),
                ('icerik', models.TextField()),
                ('yayimlanma_tarihi', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
