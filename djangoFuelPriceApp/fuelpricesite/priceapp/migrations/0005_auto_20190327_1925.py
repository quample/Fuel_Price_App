# Generated by Django 2.1.7 on 2019-03-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceapp', '0004_useraddresses_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddresses',
            name='user',
        ),
        migrations.AddField(
            model_name='useraddresses',
            name='user_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
