from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerAdminForm
from .models import Customer,CustomUser
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

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """客户表"""
    list_display = ('name','format_name','gender','phonenumber','age','qq')
    list_per_page = 5
    # 关联的字段一次性查出，减少查询次数
    list_select_related = ("user",)
    # 快捷查询(过滤器)，一般配置有choices的字段
    list_filter = ("gender",)
    # 关联搜索,模糊匹配
    # 关联表字段查询
    search_fields = ("name","user__nickname")
    # 需要编辑的字段
    fields = ('name','gender','age','phonenumber','qq',)
    # 自定义表单验证
    form = CustomerAdminForm
    # 字段脱敏处理
    def format_name(self,obj):
        return obj.name[:1] + "***"
    format_name.short_description = "用户名"





