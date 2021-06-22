# Generated by Django 2.2 on 2019-08-24 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empFName', models.CharField(max_length=50)),
                ('empLName', models.CharField(max_length=70)),
                ('empPhone', models.CharField(max_length=10)),
                ('empEmail', models.EmailField(max_length=254)),
                ('empAddress', models.TextField(max_length=50)),
                ('empGender', models.CharField(max_length=6)),
                ('empBod', models.DateTimeField(blank=True, null=True)),
                ('empMarrigStatus', models.CharField(max_length=10)),
                ('empDept', models.CharField(max_length=20)),
                ('empSalary', models.FloatField()),
                ('empDateEmpl', models.DateTimeField(blank=True, null=True)),
                ('EmpTimestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
