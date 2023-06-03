from django.contrib import admin, messages

from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """图书基础信息"""
    list_display = ('title','description','main_img','is_public','upload_date',)
    search_fields = ('title','description',)
    list_filter = ('is_hot','is_top')
    list_per_page = 10
    actions = ['disable_book','enable_book']

    def disable_book(self,request,queryset):
        queryset.update(is_public=False)
        messages.success(request,'操作成功！')
    disable_book.short_description = "批量隐藏图书"

    def enable_book(self,request,queryset):
        queryset.update(is_public=True)
        messages.success(request, '操作成功！')
    enable_book.short_description = "批量显示图书"

