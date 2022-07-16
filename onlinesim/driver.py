# -*- coding: utf-8 -*-
#
#  onlinesim.ru API client: Driver
#  Created by LulzLoL231 at 16/07/22
#
from .sms import SMSAPI
from .user import UserAPI


class OnlinesimRu:
    def __init__(self, api_key: str, lang: str = 'ru') -> None:
        self.sms = SMSAPI(api_key, lang)
        self.user = UserAPI(api_key, lang)
