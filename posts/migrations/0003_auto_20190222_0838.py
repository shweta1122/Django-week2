# Generated by Django 2.1.5 on 2019-02-22 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='User',
            new_name='user',
        ),
    ]