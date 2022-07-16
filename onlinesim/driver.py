# -*- coding: utf-8 -*-
#
#  onlinesim.ru API client: Driver
#  Created by LulzLoL231 at 16/07/22
#
from .api import APIConnector
from .sms import SMSAPI
from .user import UserAPI


class OnlinesimRu(APIConnector):
    def sms(self):
        return SMSAPI(self.api_key, self.lang)

    def user(self):
        return UserAPI(self.api_key, self.lang)
