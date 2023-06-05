from django.http import JsonResponse
from .models import Book
from django.core.paginator import Paginator

def listbooks(request):
    title_query = request.GET.get('title', '')
    img_query = request.GET.get('main_img', '')
    date_query = request.GET.get('upload_date', '')

    queryset = Book.objects.filter(
        title__icontains=title_query,
        main_img__icontains=img_query,
        upload_date__icontains=date_query
    ).values()

    pagenum = int(request.GET.get("pagenum", 1))
    pagesize = int(request.GET.get("pagesize", 10))

    pgnt = Paginator(queryset, pagesize)

    page = pgnt.page(pagenum)

    retlist = list(page.object_list)

    return JsonResponse({"ret": 0, "retlist": retlist, "total": pgnt.count()})
