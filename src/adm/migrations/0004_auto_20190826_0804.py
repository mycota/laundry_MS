# Generated by Django 2.2 on 2019-08-26 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0003_auto_20190826_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empBod',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empDateEmpl',
            field=models.DateField(null=True),
        ),
    ]
