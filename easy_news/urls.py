# -*- coding: utf-8 -*-
from django.conf.urls import *
from django.views.generic.dates import *
from django.views.generic.list import ListView
from easy_news.models import News
import datetime

from easy_news import settings as news_settings

urlpatterns = patterns('',
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})-(?P<slug>[-\w]+)/$',
        DateDetailView.as_view(queryset=News.objects.filter(show=True), date_field='date', month_format='%m',
                               slug_field='slug'), name='news_detail'),
)

if news_settings.ENABLE_NEWS_LIST:
    urlpatterns += patterns('',
        url(r'^list/$', ListView.as_view(queryset=News.objects.filter(show=True, date__lte=datetime.datetime.now)),
            name='news_list'),
    )

if news_settings.ENABLE_NEWS_ARCHIVE_INDEX:
    urlpatterns += patterns('',
        url(r'^$', ArchiveIndexView.as_view(queryset=News.objects.filter(show=True), date_field='date',
                                            context_object_name='object_list'), name='news_archive_index'),
    )

if news_settings.ENABLE_NEWS_DATE_ARCHIVE:
    urlpatterns += patterns('',
        url(r'^archive/(?P<year>\d{4})/$', YearArchiveView.as_view(queryset=News.objects.filter(show=True),
                                                                   date_field='date', make_object_list=True),
            name='news_archive_year'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})/$',
            MonthArchiveView.as_view(queryset=News.objects.filter(show=True), date_field='date', month_format='%m'),
            name='news_archive_month'),
        url(r'^archive/(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/$',
            DayArchiveView.as_view(queryset=News.objects.filter(show=True), date_field='date', month_format='%m'),
            name='news_archive_day'),
    )

if news_settings.NEWS_TAGGING:
    from tagging.views import TaggedObjectList
    urlpatterns += patterns('',
        url(r'^tag/(?P<tag>[^/]+)/$', TaggedObjectList.as_view(queryset=News.objects.filter(show=True),
                                                               paginate_by=10, allow_empty=True),
            name='news_tag_detail'),
    )
