# Generated by Django 2.2.5 on 2020-08-18 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BI', '0038_auto_20200818_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='status',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='user_dashboard',
            name='status',
            field=models.CharField(max_length=25),
        ),
    ]