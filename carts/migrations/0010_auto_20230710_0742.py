# Generated by Django 3.1 on 2023-07-10 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_reviewrating'),
        ('carts', '0009_auto_20230710_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.Variation'),
        ),
    ]