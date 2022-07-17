# -*- coding: utf-8 -*-
#
#  Onlinesim API: User API.
#  Created by LulzLoL231 at 7/7/22
#
import logging

from .api import APIConnector
from ..errors import APIError
from ..schemas import Balance


class UserAPI(APIConnector):
    log = logging.getLogger('onlinesim_api')

    async def get_balance(self) -> Balance:
        '''Returns user balance.

        Returns:
            Balance: User balance info.

        Raises:
            APIError: If API response contains error.
        '''
        self.log.debug('Called!')
        resp = self._get('getBalance')
        if resp.get('response', '-1') == '1':
            return Balance(**resp)
        else:
            raise APIError(resp.get('response', 'UnexpectedError'))
