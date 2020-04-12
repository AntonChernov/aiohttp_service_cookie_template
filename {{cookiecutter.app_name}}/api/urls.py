# -*- coding: utf-8 -*-
from aiohttp import web

from api import api

ROUTERS = [
    web.get('/api/ping', api.PingPongHandler, name='ping'),
]