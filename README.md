https://docs.djangoproject.com/zh-hans/3.2/

### 创建项目

```
django-admin startproject medpdf
```

### 创建应用

```
python manage.py startapp common
```

### 创建数据库

(medpdf)

cmd → mysql -u root -p(密码是789456)

```bash
CREATE DATABASE medpdf CHARACTER SET utf8 COLLATE utf8_general_ci;
```

配置数据库信息（settings文件中）

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medpdf',
        'USER': 'root',
        'PASSWORD': '789456',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
        },
    }
}
```

定义数据模型（common/models.py）

```python
from django.db import models
class Customer(models.Model):
    # 客户名称
    name = models.CharField(max_length=200)

    # 性别选项
    GENDER_CHOICES = (
        ('male', '男性'),
        ('female', '女性'),
    )
    # 性别
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    # 联系电话
    phonenumber = models.CharField(max_length=200)
```

注册app(settings.py中)

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    #或者
    'common.apps.CommonConfig',
]
```

### 生成表并迁移

```python
python manage.py makemigrations common
python manage.py migrate
```

打开navcat查看数据库

### 创建超级管理员

```
python manage.py createsuperuser
liubo/789456
```

启动项目

```py
python manage.py runserver 8080
```

登录后台管理页面

```py
http://127.0.0.1:8080/admin/login/
liubo/789456
```



### 模型添加到后台

实现使用admin后台进行增删改查

```python
# common/models.py
from django.db import models
class Customer(models.Model):
    # 客户名称
    name = models.CharField('姓名',max_length=200)
    # 性别选项
    GENDER_CHOICES = (
        ('male', '男性'),
        ('female', '女性'),
    )
    # 性别
    gender = models.CharField('性别',max_length=10, choices=GENDER_CHOICES)

    # 联系电话
    phonenumber = models.CharField('电话',max_length=200)

    # qq号码
    QQ = models.CharField('QQ号',max_length=200)
    # 填写verbose_name参数后后台会用这个字段替换name,gender这些英文字段
    # 设置后后台会显示对象的名字，而不是原始的object(1,2,2)
    def __str__(self):
        return self.name
```

```py
# common/admin.py
from django.contrib import admin
from .models import Customer
# admin.site.register(Customer)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('name','gender','phonenumber','QQ')
```

### 语言本地化

设置语言为中文（语言本地化）

设置中国时区（时间本地化）

```py
# settings.py
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
# models.py
verbose_name = "用户详细信息" # 后台显示中文字段
```

```py
# common/apps.py
from django.apps import AppConfig
class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
    verbose_name = "公共模块"
```

```py
# common/models.py
from django.db import models
class Customer(models.Model):
    # 客户名称
    name = models.CharField(verbose_name='姓名',max_length=200)
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
    QQ = models.CharField(verbose_name='QQ号',max_length=200)
    # 填写verbose_name参数后后台会用这个字段替换name,gender这些
    # 设置后后台会显示对象的名字，而不是原始的object(1,2,2)
    class Meta:
        db_table = "common_customer"
        verbose_name = "客户信息表"
        verbose_name_plural = "客户信息表"
    def __str__(self):
        return self.name
```

### AbstractUser

### OneToOneField

给Django自带的user表增加一些字段，并关联到自定义用户模型

```py
# common/models.py
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
    QQ = models.CharField(verbose_name='QQ号',max_length=200)
    # 填写verbose_name参数后后台会用这个字段替换name,gender这些
    # 设置后后台会显示对象的名字，而不是原始的object(1,2,2)
    class Meta:
        db_table = "common_customer"
        verbose_name = "客户信息表"
        verbose_name_plural = "客户信息表"
    def __str__(self):
        return self.name

```

```py
# settings.py
# 设置自定义的用户模型
AUTH_USER_MODEL = 'common.CustomUser'
```

### 优化 脱敏 查询 

```py
from django.contrib import admin
from .models import Customer,CustomUser
# admin.site.register(Customer)

@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('nickname','avatar','is_active')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('name','format_name','gender','phonenumber','QQ')
    list_per_page = 3
    # 进入界面一次性查询关联表，外键关联查询优化
    list_select_related = ("user",)
    # 快捷查询(过滤器)，一般配置有choices的字段
    list_filter = ("gender",)
    # 关联搜索,模糊匹配
    # 关联表字段查询
    search_fields = ("name","user__nickname")
    # 字段脱敏处理
    def format_name(self,obj):
        return obj.name[:1] + "***"
    # 格式化后的字段名取个别名
    format_name.short_description = "用户名"
```



