"""
ASGI config for src project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter

from django.core.asgi import get_asgi_application
launch_point = os.environ.get('LAUNCH_POINT', 'local')
if launch_point == 'stand':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.stand')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.local')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
})

