# Generated by Django 2.2 on 2019-08-27 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190827_0608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeeinfo',
            old_name='empRole',
            new_name='emp_Role',
        ),
    ]