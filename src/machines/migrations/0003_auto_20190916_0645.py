# Generated by Django 2.2 on 2019-09-16 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_machines_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='machines',
            old_name='mac_name',
            new_name='machine_name',
        ),
        migrations.RenameField(
            model_name='machines',
            old_name='manufactural',
            new_name='manufacturer',
        ),
    ]
