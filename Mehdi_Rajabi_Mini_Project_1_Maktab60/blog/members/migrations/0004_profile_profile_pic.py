# Generated by Django 3.2.9 on 2021-12-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile_pictures', verbose_name='عکس پروفایل'),
        ),
    ]
