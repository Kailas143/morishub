# Generated by Django 3.2.10 on 2021-12-14 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='phno',
            field=models.CharField(max_length=10),
        ),
    ]