from ckeditor.fields import RichTextField
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="书名")
    author = models.CharField(max_length=255, verbose_name="作者",null=True, blank=True)
    description = models.TextField(verbose_name="描述",null=True, blank=True)
    main_img = models.ImageField(verbose_name="主图",upload_to='%Y%m/book/',max_length=256,null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, verbose_name="上传日期",null=True, blank=True)
    file_type = models.CharField(max_length=50, verbose_name="文件类型",null=True, blank=True)
    category = models.CharField(max_length=50, verbose_name="分类",null=True, blank=True)
    tags = models.CharField(max_length=255, verbose_name="标签",null=True, blank=True)
    file_size = models.PositiveIntegerField(verbose_name="文件大小",null=True, blank=True)
    download_count = models.PositiveIntegerField(default=0, verbose_name="下载量",null=True, blank=True)
    favorite_count = models.PositiveIntegerField(default=0, verbose_name="收藏量",null=True, blank=True)
    is_public = models.BooleanField(default=True, verbose_name="是否公开",null=True, blank=True)
    is_top = models.BooleanField(default=True, verbose_name="是否为精选图书",null=True, blank=True)
    is_hot = models.BooleanField(default=True, verbose_name="是否为热门图书",null=True, blank=True)
    # uploader = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="上传者",null=True, blank=True)
    # 加上存放详情页富文本的字段
    # detail_page_content = models.TextField(verbose_name="详情页富文本内容",null=True, blank=True)
    detail_page_content = RichTextField(verbose_name="详情页富文本内容",null=True, blank=True)

    class Meta:
        verbose_name = "PDF书籍"
        verbose_name_plural = "PDF书籍"

    def __str__(self):
        return self.title