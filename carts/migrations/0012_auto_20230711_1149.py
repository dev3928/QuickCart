# Generated by Django 3.1 on 2023-07-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_productgallery'),
        ('carts', '0011_auto_20230711_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]