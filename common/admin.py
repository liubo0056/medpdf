from django.contrib import admin

from .forms import CustomerAdminForm
from .models import Customer,CustomUser
# admin.site.register(Customer)

@admin.register(CustomUser)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('nickname','avatar','is_active')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('name','format_name','gender','phonenumber','age','qq')
    list_per_page = 3
    # 关联的字段一次性查出，减少查询次数
    list_select_related = ("user",)
    # 快捷查询(过滤器)，一般配置有choices的字段
    list_filter = ("gender",)
    # 关联搜索,模糊匹配
    # 关联表字段查询
    search_fields = ("name","user__nickname")
    # 需要编辑的字段
    fields = ('name','age','phonenumber','qq',)
    # 表单验证（age字段）
    form = CustomerAdminForm
    # 字段脱敏处理
    def format_name(self,obj):
        return obj.name[:1] + "***"
    format_name.short_description = "用户名"





