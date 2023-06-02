from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # 添加您需要的额外字段
    avatar = models.ImageField('用户头像', upload_to='avatar/%Y%m', null=True, blank=True)
    nickname = models.CharField('昵称', max_length=32, unique=True)

    # 如果需要在后台显示用户的某些字段，还需设置相应的方法，例如：
    def __str__(self):
        return self.nickname

class Customer(models.Model):
    user = models.OneToOneField(CustomUser,related_name='customer',on_delete=models.CASCADE,null=True, blank=True)
    # 客户名称
    name = models.CharField(verbose_name='姓名',max_length=200)
    # 年龄
    age = models.IntegerField(verbose_name='年龄',null=True, blank=True)
    # 性别选项
    GENDER_CHOICES = (
        ('male', '男性'),
        ('female', '女性'),
    )
    # 性别
    gender = models.CharField(verbose_name='性别',max_length=10, choices=GENDER_CHOICES)

    # 联系电话
    phonenumber = models.CharField(verbose_name='电话',max_length=200)

    # qq号码
    qq = models.CharField(verbose_name='QQ号',max_length=200)
    # 填写verbose_name参数后后台会用这个字段替换name,gender这些
    # 设置后后台会显示对象的名字，而不是原始的object(1,2,2)
    class Meta:
        db_table = "common_customer"
        verbose_name = "客户信息表"
        verbose_name_plural = "客户信息表"
    def __str__(self):
        return self.name
