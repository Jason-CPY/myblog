# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Article
from models import Category
from models import Tag


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')
    list_filter = ('pub_time', )


admin.site.register([Category, Tag, Article])
