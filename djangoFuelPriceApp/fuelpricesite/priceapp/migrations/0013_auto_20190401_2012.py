# Generated by Django 2.1.7 on 2019-04-02 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0012_auto_20190330_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquotes',
            name='reqDelDate',
            field=models.DateField(default='MM/DD/YYYY', verbose_name='Delivery Date'),
        ),
    ]