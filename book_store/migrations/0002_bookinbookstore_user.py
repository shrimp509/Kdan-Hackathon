# Generated by Django 3.1 on 2020-08-22 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_store', '0001_initial'),
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinbookstore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user'),
        ),
    ]
