# -*- coding: utf-8 -*-
#
#  Onlinesim API.
#  Created by LulzLoL231 at 7/7/22
#
import logging
from urllib.parse import urlencode

from aiohttp import ClientSession


class APIError(Exception):
    pass


class APIConnector:
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
        'Accept': 'application/json'
    }
    log = logging.getLogger('onlinesim_api')

    def __init__(self, api_key: str, lang: str = 'ru') -> None:
        self.api_key = api_key
        self.lang = lang

    async def _get(self, endpoint: str, **params) -> dict:
        '''Makes a request to API.

        Args:
            endpoint (str): API endpoint.
            params (dict, optional): API params.

        Returns:
            dict: API response.

        Raises:
            APIError: If API request is unsuccessfull.
        '''
        self.log.debug(f'Called with args: ({endpoint}, {params})')
        query = {k: v for k, v in params.items() if v is not None}
        query['lang'] = self.lang
        query['apikey'] = self.api_key
        url = f'https://onlinesim.ru/api/{endpoint}.php?{urlencode(query)}'
        async with ClientSession(headers=self.HEADERS) as sess:
            async with sess.get(url) as req:
                if req.ok:
                    resp = await req.json()
                    self.log.debug(f'API response: {resp}')
                    return resp
                else:
                    resp_text = await req.text()
                    self.log.error(f'Unsuccessfull request to API [{req.status}]: {resp_text}')
                    raise APIError('Unsuccessfull API request!')
