# Generated by Django 2.1.7 on 2019-04-13 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0016_auto_20190404_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddresses',
            name='full_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Full Name'),
        ),
    ]