# Generated by Django 3.1.7 on 2021-09-14 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210320_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='myprofile.png', upload_to='profilePicture'),
        ),
    ]