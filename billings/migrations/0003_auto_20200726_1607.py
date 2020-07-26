# Generated by Django 3.0.8 on 2020-07-26 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billings', '0002_auto_20200726_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='products',
        ),
        migrations.AddField(
            model_name='transaction',
            name='biling_profile',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='billings.Billing'),
            preserve_default=False,
        ),
    ]