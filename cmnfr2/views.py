# -*- coding: utf-8 -*-
__author__ = 'weather'

from django.shortcuts import render
from models import MainPage
from django.utils.translation import get_language


def main(request):
    lang = get_language().upper()
    mainpage = MainPage.objects.filter(lang=lang)[0]
    title = mainpage.title
    bar_list = mainpage.bar_title.split(" ")
    param  = {
        "title": title,
        "barlist": bar_list
    }
    return render(request, "example.html", param)