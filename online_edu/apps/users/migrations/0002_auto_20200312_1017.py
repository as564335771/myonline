# Generated by Django 2.0.2 on 2020-03-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='', upload_to='image/%Y/%m'),
        ),
    ]
