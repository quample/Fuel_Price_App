# Generated by Django 2.1.7 on 2019-04-16 05:35

import django.core.validators
from django.db import migrations, models
import priceapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0017_auto_20190413_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquotes',
            name='pricePerGal',
            field=models.FloatField(default='0.00', verbose_name='Suggested Price'),
        ),
        migrations.AddField(
            model_name='userquotes',
            name='totalPrice',
            field=models.FloatField(default='0.00', verbose_name='Suggested Price'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_City',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alpha characters are allowed.')], verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_P',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Address 1'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_P2',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Address 2'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_State',
            field=models.CharField(max_length=2, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alpha characters are allowed.')], verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_Zip',
            field=models.CharField(max_length=9, validators=[priceapp.models.min_len, django.core.validators.RegexValidator('^[0-9]*$', 'Only numeric characters are allowed.')], verbose_name='Zip code'),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='ad_full',
            field=models.CharField(default=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Address 1'), max_length=250),
        ),
        migrations.AlterField(
            model_name='useraddresses',
            name='full_name',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')], verbose_name='Full Name'),
        ),
    ]
