"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
import myapp.routing
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
 'http':get_asgi_application(),
 "websocket": AuthMiddlewareStack(   # For Websocket Connection
        URLRouter(
            myapp.routing.websocket_urlpatterns
        )
),
})