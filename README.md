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



### 模型添加到后台(ModelAdmin)

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
# common/admin.py
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

### 限制可编辑字段

是否允许编辑字段

```python
# models.py
editable=False
```

fields/exclude 需要编辑/不需要编辑的字段列表(#/common/admin.py)

### 表单验证实现

```python
# common/forms.py

from django import forms
from .models import Customer
class CustomerAdminForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"
    def clean_age(self):
        age = self.cleaned_data["age"]
        if int(age) >=120 or int(age) <= 1:
            raise forms.ValidationError("年龄只能在1-120之间")
        return age
```

```python
# common/admin.py
form = CustomerAdminForm
```

### 重写保存方法

做一些业务逻辑处理

```py
    # forms.py
    def save(self,commit=False):
        obj = super().save(commit=commit)
        if obj.age <=5:
            obj.age = 18
            obj.save()
        return obj
```

### 用户后台管理（UserAdmin）

```python
# common/admin.py
from django.contrib.auth.admin import UserAdmin
@admin.register(CustomUser)
class MyUserAdmin(UserAdmin):
    """用户基础信息管理"""
    # 列表中显示的内容
    list_display = ('username', 'nickname', 'is_active', 'is_staff','is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'nickname')
    # 新增用户的表单
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('nickname',)}),
    )
    # 修改用户的表单
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('nickname','avatar',)}),
    )
    actions = ['disable_user','enable_user']

    def disable_user(self,request,queryset):
        queryset.update(is_active=False)
    disable_user.short_description = "批量禁用用户"

    def enable_user(self,request,queryset):
        queryset.update(is_active=True)
    enable_user.short_description = "批量启用用户"
```

### 富文本功能实现

https://github.com/django-ckeditor/django-ckeditor

```bash
pip install django-ckeditor
Add "ckeditor" to your INSTALLED_APPS setting.
Run the collectstatic management command: $ ./manage.py collectstatic. 
```

> 直接运行python manage.py会有代码提示

```py
# settings.py
INSTALLED_APPS = [
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 富文本编辑器文件上传位置
CKEDITOR_UPLOAD_PATH = "uploads/"
MEDIA_URL = 'http://localhost:8080/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# models.py
detail_page_content = RichTextField(verbose_name="详情页富文本内容",null=True, blank=True)
```

### media文件夹路由设置

```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/common/', include("common.urls")),
    path('api/books/', include("books.urls")),
    url(r'^media/(?P<path>.*)', serve, {"document_root":settings.MEDIA_ROOT}),
    # 富文本相关配置
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static("/", document_root="./z_dist")
```

### 登录页面测试

```javascript
    <script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
    <script>
        window.onload = () => {
            document.querySelector('#loginBtn').onclick = () => {
                let username = document.querySelector('#username').value
                let password = document.querySelector('#password').value
                $.post('/api/common/signin',
                    {
                        username: username,
                        password: password
                    }
                )
            }
        }
    </script>
```

```html
<body>
    <main>
        <div>用户登录</div>
        <div>
            <label for="username"></label><input type="text" placeholder="请输入用户名" id="username">
            <label for="password"></label><input type="password" placeholder="请输入密码" id="password">
            <button id="loginBtn">登录</button>
        </div>
        <a href="#">还没有账号？请先注册</a>
    </main>
</body>
```

### 分页功能

```python
from django.http import JsonResponse # 导入JsonResponse模块，用于返回JSON格式的响应
from django.core.paginator import Paginator # 导入Paginator模块，用于分页
from .models import Book # 导入Book模型

def listbooks(request): 
    title_query = request.GET.get('title', '') # 获取GET请求中的'title'参数
    img_query = request.GET.get('main_img', '') # 获取GET请求中的'main_img'参数
    date_query = request.GET.get('upload_date', '') # 获取GET请求中的'upload_date'参数

    books_qs = Book.objects.filter( # 通过filter方法过滤数据
        title__icontains=title_query, # 根据title_query进行模糊查询
        main_img__icontains=img_query, # 根据img_query进行模糊查询
        upload_date__icontains=date_query # 根据date_query进行模糊查询
    )
    pagesize = request.GET.get('pagesize') # 获取GET请求中的'pagesize'参数

    paginator = Paginator(books_qs, pagesize) # 创建Paginator对象，每页显示pagesize条数据

    page_number = request.GET.get('pagenum') # 获取GET请求中的'pagenum'参数
    page_obj = paginator.get_page(page_number) # 获取指定页数的Page对象

    books_list = list(page_obj.object_list.values()) # 将Page对象转换为可迭代的列表

    return JsonResponse({ # 返回JSON格式的响应
        'books': books_list, # 列表数据
        'has_previous': page_obj.has_previous(), # 是否有前一页
        'has_next': page_obj.has_next(), # 是否有后一页
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None, # 前一页页码
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None, # 后一页页码
        'total_pages': paginator.num_pages, # 总页数
        'current_page_number': page_obj.number, # 当前页码
    }, safe=False) # 设置safe为False，使得可以返回非字典类型的数据
```

### requests构建请求

```python
import requests, pprint
payload = { "pagenum": 1,"pagesize":5}
response = requests.get(
    "http://127.0.0.1/api/books/books",
    params=payload
)
pprint.pprint(response.json())
```

### 重定向实现

```javascript
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js"></script>
    <script>
        window.onload = () => {
            document.querySelector('#loginBtn').onclick = () => {
                let username = document.querySelector('#username').value
                let password = document.querySelector('#password').value
                $.ajax({
                    url: '/api/common/signin',
                    method: 'POST',
                    data: {
                        username: username,
                        password: password
                    },
                    success: function (data, status) {
                        // 当服务器成功响应请求时调用此函数
                        // 把响应数据data(object)序列化显示
                        // const json = JSON.stringify(data)
                        console.log('响应数据: ' + data.ret);
                        console.log('状态: ' + status);
                        //如果登录成功，重定向至另外一个页面
                        if (data.ret === 0) {
                            location.href = './admin/'
                        }
                        else { alert('登录失败' + data.msg) }
                    },
                    error: function (xhr, status, error) {
                        // 当请求发生错误时调用此函数
                        console.log('错误: ' + error);
                    }
                })
            }
        }
    </script>
```

### grid实现整体布局

```html
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>管理页面</title>
    <style>
        body {
            /* 高度占满整个屏幕 */
            height: 100vh;
            margin: 0;
            /* 指定网格布局 */
            display: grid;
            /* 指定行的分布 */
            grid-template-rows: auto 1fr auto;
            grid-template-columns: 20rem 1fr;
        }

        div {
            border: 1px solid red;
        }
    </style>
</head>
<body>
    <div class="nav-logo">管理员操作</div>
    <div>导航栏</div>
    <div>操作菜单</div>
    <div>正文</div>
    <div></div>
    <div>页脚</div>
</body>
```

