# 导入 Customer 对象定义
from django.http import JsonResponse
from .models import Book
"""版本一-全部列出"""
# def listbooks(request):
#     queryset = Book.objects.values()
#     books_list = list(queryset)  # 转换为可迭代的列表
#     return JsonResponse(books_list, safe=False)

"""版本二-增加过滤条件"""
# def listbooks(request):
#     queryset = Book.objects.filter(title__icontains=request.GET.get('title','')).values()
#     books_list = list(queryset)  # 转换为可迭代的列表
#     return JsonResponse(books_list, safe=False)

"""版本三-多个字段参与检索"""
def listbooks(request):
    title_query = request.GET.get('title', '')
    img_query = request.GET.get('main_img', '')
    date_query = request.GET.get('upload_date', '')

    queryset = Book.objects.filter(
        title__icontains=title_query,
        main_img__icontains=img_query,
        upload_date__icontains=date_query
    ).values()
    books_list = list(queryset)  # 转换为可迭代的列表
    return JsonResponse(books_list, safe=False)
