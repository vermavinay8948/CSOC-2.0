# Generated by Django 2.2.2 on 2019-07-21 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_departments_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='year',
        ),
        migrations.AddField(
            model_name='subject',
            name='semester',
            field=models.CharField(blank=True, choices=[('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eigth', 'Eigth'), ('ninth', 'Ninth')], max_length=20, null=True),
        ),
    ]
