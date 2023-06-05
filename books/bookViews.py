from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Book

def listbooks(request):
    title_query = request.GET.get('title', '')
    img_query = request.GET.get('main_img', '')
    date_query = request.GET.get('upload_date', '')

    books_qs = Book.objects.filter(
        title__icontains=title_query,
        main_img__icontains=img_query,
        upload_date__icontains=date_query
    )
    pagesize = request.GET.get('pagesize')

    paginator = Paginator(books_qs, pagesize) # 每页显示10条数据

    page_number = request.GET.get('pagenum')
    page_obj = paginator.get_page(page_number)

    books_list = list(page_obj.object_list.values()) # 转换为可迭代的列表

    return JsonResponse({
        'books': books_list,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'previous_page_number': page_obj.previous_page_number() if page_obj.has_previous() else None,
        'next_page_number': page_obj.next_page_number() if page_obj.has_next() else None,
        'total_pages': paginator.num_pages,
        'current_page_number': page_obj.number,
    }, safe=False)