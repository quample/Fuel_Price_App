# Generated by Django 2.1.7 on 2019-03-27 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddresses',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserAddresses',
        ),
    ]