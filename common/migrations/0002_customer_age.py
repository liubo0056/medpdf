# Generated by Django 3.2 on 2023-06-02 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
    ]