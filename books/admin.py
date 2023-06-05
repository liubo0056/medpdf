from django.contrib import admin, messages

from .models import Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """图书基础信息"""
    list_display = ('book_id','title','category','main_img','is_public','is_top')
    search_fields = ('title',)
    list_filter = ('is_hot','is_top')
    list_per_page = 10
    actions = ['disable_book','enable_book']
    fieldsets = (
        ('基本信息', {
            'fields': ('book_id', 'title', 'main_img')
        }),
        ('文件信息', {
            'fields': ('file_type', 'file_size')
        }),
        ('其他信息', {
            'fields': ('category', 'price', 'is_public', 'is_top', 'is_hot', 'download_count', 'favorite_count')
        }),
        ('详情页内容', {
            'fields': ('detail_page_content',)
        }),
        ('下载地址', {
            'fields': ('download_path',)
        })
    )

    def disable_book(self,request,queryset):
        queryset.update(is_public=False)
        messages.success(request,'操作成功！')
    disable_book.short_description = "批量隐藏图书"

    def enable_book(self,request,queryset):
        queryset.update(is_public=True)
        messages.success(request, '操作成功！')
    enable_book.short_description = "批量显示图书"
