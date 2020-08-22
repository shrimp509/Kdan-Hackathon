# Generated by Django 3.1 on 2020-08-22 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.TextField()),
                ('cash_balance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_amount', models.FloatField()),
                ('transaction_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.book')),
                ('book_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_store.bookstore')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user')),
            ],
        ),
    ]