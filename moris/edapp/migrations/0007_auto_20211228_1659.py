# Generated by Django 3.2.10 on 2021-12-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edapp', '0006_auto_20211228_1633'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='fb_link',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='linkdin_link',
            field=models.URLField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='twitt_link',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
