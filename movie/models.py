from django.db import models


# Create your models here.
class Categroys(models.Model):
    categroy = models.CharField(max_length=15, verbose_name='影片分类')

    def __str__(self):
        return self.categroy

    class Meta:
        verbose_name = '影片分类'
        verbose_name_plural = verbose_name


class M_info(models.Model):
    name = models.CharField(max_length=10, verbose_name='影片名')

    category = models.ForeignKey(Categroys, on_delete=models.DO_NOTHING, verbose_name='影片分类')
    score = models.CharField(max_length=5, default='6.0', verbose_name='评分')
    director = models.CharField(max_length=30, default='未知', verbose_name='导演')
    scriptwriter = models.CharField(max_length=10, default='未知', verbose_name='编剧')
    actors = models.CharField(max_length=20, blank=True, default='未知', verbose_name='主演')
    country = models.CharField(max_length=10, default='未知', verbose_name='国家')

    language = models.CharField(max_length=20, default='未知', verbose_name='语言')
    time = models.CharField(max_length=15, default='未知', verbose_name='时长')
    contends = models.TextField(max_length=300, default='暂无', verbose_name='简介')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='加入时间')
    last_update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_time']
        verbose_name = '电影信息'
        verbose_name_plural = verbose_name
