# Generated by Django 2.2 on 2019-08-26 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm', '0002_auto_20190826_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='empBod',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empDateEmpl',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
