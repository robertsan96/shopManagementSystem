# Generated by Django 2.0.1 on 2018-01-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_item_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
