# Generated by Django 4.2.1 on 2024-08-05 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clips', '0004_animeseries_image_url_animeseries_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='download_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
