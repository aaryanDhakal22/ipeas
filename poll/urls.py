# Copyright (c) 2022 aaryan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from django.urls import path

from .views import homepage, pollpage, resultpage

urlpatterns = [
    path("", homepage, name="home"),
    path("poll", pollpage, name="poll"),
    path("results", resultpage, name="result"),
]
