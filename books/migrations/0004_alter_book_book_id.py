# Generated by Django 3.2 on 2023-06-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_file_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_id',
            field=models.CharField(max_length=255, verbose_name='图书编号'),
        ),
    ]
