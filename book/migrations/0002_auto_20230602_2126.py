# Generated by Django 3.2 on 2023-06-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfbook',
            name='author',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='category',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='分类'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='detail_page_content',
            field=models.TextField(blank=True, null=True, verbose_name='详情页富文本内容'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='download_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='下载量'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='favorite_count',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='收藏量'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='file_size',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='文件大小'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='file_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='文件类型'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='is_public',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='是否公开'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='tags',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='标签'),
        ),
        migrations.AlterField(
            model_name='pdfbook',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='上传日期'),
        ),
    ]
