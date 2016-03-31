# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Article, MainPage

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(MainPage)
class MainPageAdmin(admin.ModelAdmin):
    pass