# Generated by Django 3.0.8 on 2021-02-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customadmin', '0003_frontendsettings_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontendsettings',
            name='currency',
            field=models.CharField(choices=[('TK', 'TK(BDT)'), ('$', '$(USA)')], default='TK', max_length=2),
        ),
    ]
