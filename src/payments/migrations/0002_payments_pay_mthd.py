# Generated by Django 2.2 on 2019-09-09 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payments',
            name='pay_mthd',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
