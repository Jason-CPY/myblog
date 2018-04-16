# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('名称', max_length=16)

    def __unicode__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('标题', max_length=32)
    author = models.CharField('作者', max_length=16)
    content = models.TextField('正文')
    pub_time = models.DateTimeField('发布时间', auto_now_add=True)
    overview = models.CharField('预览', max_length=32, default='Overview')
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category, verbose_name='分类')
    tags = models.ManyToManyField(Tag, verbose_name='标签')

    def __unicode__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])
# class Article(models.Model):
#     title = models.CharField(max_length=32, default='Title')
#     content = models.TextField(null=True)
#     pub_time = models.DateTimeField(auto_now_add=True)

