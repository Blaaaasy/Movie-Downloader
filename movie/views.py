from django.shortcuts import render
from .models import M_info, Categroys
from django.core.paginator import Paginator


# Create your views here.
def movies_list_common_command(request, movies_all_list):  # 分页功能需要用的方法
    paginator = Paginator(movies_all_list, 20)  # 20个人一页
    page_num = request.GET.get('page', 1)  # 得参
    page_of_movies = paginator.get_page(page_num)
    current_page_num = page_of_movies.number
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))  # 获取页码范围

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if page_range[-1] + 2 <= paginator.num_pages:
        page_range.append('...')  # 添加省略号

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)  # 加上首页和尾页

    #  时间统计
    movie_dates = M_info.objects.dates('created_time', 'month', order='DESC')
    movie_dates_dict = {}
    for movie_date in movie_dates:
        movie_count = M_info.objects.filter(created_time__year=movie_date.year,
                                            created_time__month=movie_date.month).count()
        movie_dates_dict[movie_date] = movie_count

    context = {}
    categroys_list_all = Categroys.objects.all()
    context['categroys_list_all'] = categroys_list_all
    context['movies'] = page_of_movies.object_list
    context['page_of_movies'] = page_of_movies
    context['categroys'] = Categroys.objects.all()
    context['page_range'] = page_range
    context['movie_dates'] = movie_dates_dict
    return context


def movies_list(request):
    context = {}

    movies_all_list = M_info.objects.filter(is_delete=False)
    # categroys_list_all = Categroys.objects.all()
    # context['categroys_list_all'] = categroys_list_all
    context = movies_list_common_command(request, movies_all_list)
    return render(request, 'movie/movie_list.html', context)
