# Generated by Django 2.0.1 on 2018-01-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='short_description',
            field=models.TextField(default='dsdasdas'),
            preserve_default=False,
        ),
    ]