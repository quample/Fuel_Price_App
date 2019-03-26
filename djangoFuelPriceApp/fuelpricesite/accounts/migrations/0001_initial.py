# Generated by Django 2.1.7 on 2019-03-21 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_P', models.CharField(max_length=100)),
                ('ad_P2', models.CharField(max_length=100)),
                ('ad_City', models.CharField(max_length=100)),
                ('ad_State', models.CharField(max_length=2)),
                ('ad_Zip', models.CharField(max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]