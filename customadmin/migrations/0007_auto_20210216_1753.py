# Generated by Django 3.0.8 on 2021-02-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0006_auto_20210216_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='thumbnail',
            new_name='thumbnail_one',
        ),
        migrations.AddField(
            model_name='about',
            name='thumbnail_three',
            field=models.ImageField(default=1, upload_to='photos/about/%Y-%m-%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='thumbnail_two',
            field=models.ImageField(default=1, upload_to='photos/about/%Y-%m-%d/'),
            preserve_default=False,
        ),
    ]