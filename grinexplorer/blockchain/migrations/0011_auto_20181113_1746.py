# Generated by Django 2.1.1 on 2018-11-13 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0010_auto_20181030_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='total_difficulty',
            field=models.BigIntegerField(),
        ),
    ]
