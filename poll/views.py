# Copyright (c) 2022 aaryan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, "homepage.html")


def pollpage(request):
    return render(request, "homepage.html")


def resultpage(request):
    return render(request, "homepage.html")
