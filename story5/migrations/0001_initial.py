# Generated by Django 3.1.1 on 2020-10-12 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MataKuliah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_matkul', models.CharField(max_length=50)),
                ('semester', models.CharField(max_length=50)),
                ('deskripsi', models.TextField(max_length=200)),
            ],
        ),
    ]
