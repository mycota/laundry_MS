# Generated by Django 2.2 on 2019-08-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20190828_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeinfo',
            name='address',
            field=models.TextField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='gender',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='marrig_Status',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employeeinfo',
            name='role',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
