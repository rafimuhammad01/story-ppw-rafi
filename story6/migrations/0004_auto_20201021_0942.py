# Generated by Django 3.1.1 on 2020-10-21 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story6', '0003_auto_20201020_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatan',
            name='peserta',
            field=models.ManyToManyField(blank=True, to='story6.Person'),
        ),
    ]