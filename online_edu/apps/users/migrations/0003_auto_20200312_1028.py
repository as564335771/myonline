# Generated by Django 2.0.2 on 2020-03-12 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200312_1017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='image/%Y/%m'),
        ),
    ]