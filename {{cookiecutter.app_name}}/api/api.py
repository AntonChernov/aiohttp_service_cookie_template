# -*- coding: utf-8 -*-
import datetime

from aiohttp import web

from log import _log as log


class PingPongHandler(web.View):

    async def get(self, ):
        return web.json_response({'Ping': 'Pong'})
