# Generated by Django 3.1.4 on 2020-12-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar.jpg', null=True, upload_to='customers'),
        ),
    ]
