# Generated by Django 2.2.2 on 2019-06-29 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
