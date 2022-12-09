# Copyright (c) 2022 aaryan
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""
ASGI config for ipeas project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ipeas.settings")

application = get_asgi_application()
