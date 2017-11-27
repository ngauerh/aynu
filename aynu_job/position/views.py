from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
# Create your views here.
from .models import Work


# 首页
def index(request):
    return render(request, 'index.html')


# 搜索
def work_search(request, pIndex=1):
    search_key = request.GET.get('search')
    work_list = Work.objects.all()
    if request.GET.get('search', '') != '':
        work_list = Work.objects.filter(Q(job_comp__icontains=search_key) | Q(job_name__icontains=search_key))

    if len(work_list) != 0:
        # 分页,传入数据和页的大小来创建对象
        p = Paginator(work_list, 10)
        # 判断页号没有初始值时初始化1
        if pIndex == '':
            pIndex = '1'
        pIndex = int(pIndex)  # 类型转换int
        list2 = p.page(pIndex)  # 获取当前页数据
        plist = p.page_range  # 获取页码信息
        # 封装分页信息
        context = {'work_list': list2, 'plist': plist, 'pIndex':  pIndex, 'where': search_key, 'lenlist': len(work_list)}
        return render(request, 'search.html', context)
    else:
        return HttpResponse('没有搜索结果')


# 详情
def details(request, wid):
    ob = Work.objects.get(id=wid)
    context = {'ob_list': ob}
    return render(request, 'details.html', context)
