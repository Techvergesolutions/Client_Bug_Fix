# Generated by Django 2.2.5 on 2020-09-17 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BI', '0049_role_user_roles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='group_id',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='user_roles',
            old_name='role_id',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='user_roles',
            old_name='user_id',
            new_name='user',
        ),
    ]