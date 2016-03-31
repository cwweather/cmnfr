# -*- coding: utf-8 -*-
from django.db import models


LANG = (
    ('ZH-CN', 'ZH-CN'),
    ('EN', 'EN'),
    ('FR', 'FR'),
)


class MainPage(models.Model):
    title = models.CharField(u'标题', max_length=800)
    subtitle = models.CharField(u'副标题', max_length=1000)
    lang = models.CharField(u'语言代码', choices=LANG, default='ZH-CN', max_length=30)
    bar_title = models.CharField(u'菜单列表', max_length=1000)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间' ,auto_now=True, null=True)
    create_time = models.DateTimeField(u'创建时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(u'标题', max_length=800)
    subtitle = models.CharField(u'副标题', max_length=1000)
    lang = models.CharField(u'语音代码', max_length=50)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间' ,auto_now=True, null=True)
    create_time = models.DateTimeField(u'创建时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title