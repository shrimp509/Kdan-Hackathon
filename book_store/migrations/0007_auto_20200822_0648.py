# Generated by Django 3.1 on 2020-08-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0006_auto_20200822_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openinghour',
            name='close_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='openinghour',
            name='open_time',
            field=models.DateTimeField(),
        ),
    ]