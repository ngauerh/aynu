from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),  # 网站首页
    url(r'^search(?P<pIndex>[0-9]+)$', views.work_search, name='work_search'),  # 网站首页
    url(r'^details/(?P<wid>[0-9]+)$', views.details, name='work_details'),  # 工作详情
]
