# -*- coding: utf-8 -*-
#
#  Onlinesim API: SMS API.
#  Created by LulzLoL231 at 7/7/22
#
import logging
from typing import Literal

from ..errors import APIError
from .api import AsyncAPIConnector
from ..schemas import NumbersStats, State


class SMSAPI(AsyncAPIConnector):
    log = logging.getLogger('onlinesim_api')

    async def get_numbers_stats(self) -> NumbersStats:
        '''Получение актуальной статистики по странам и количеству номеров

        Returns:
            NumbersStats: Статистика.
        '''
        self.log.debug('Called!')
        resp = await self._get('getNumbersStats')
        return NumbersStats(**resp)

    async def get_num(self, service: str) -> int:
        '''Делает запрос виртуального номера, создает операцию (сохраняет список параметров запроса).

        Args:
            service (str): определяет сайт (сервис) от которого будет ожидаться и отображаться СМС

        Returns:
            int: tzid.
        '''
        self.log.debug(f'Called with args: ({service})')
        resp = await self._get('getNum', service=service)
        if resp.get('response', '-1') == 1:
            return resp.get('tzid', -1)
        else:
            raise APIError(resp.get('response', 'UnexpectedError'))

    async def get_state(
        self, tzid: int | None = None, message_to_code: int | None = None,
        msg_list: int | None = None, clean: int | None = None
    ) -> list[State]:
        '''Возвращает состояние выбранной операции или всех заказанных операций.

        Args:
            tzid (int | None, optional): Идентификатор операции. Defaults to None.
            message_to_code (int | None, optional): 1 - показывать только код из СМС, 0 - показывать СМС полностью. Defaults to None.
            msg_list (int | None, optional): Тип списка сообщений, 1 - список, 0 - активное сообщение. Defaults to None.
            clean (int | None, optional): 1 - не показывать сообщения по кругу, работает только при msg_list=0. Defaults to None.

        Returns:
            list[State]: Массив состояний операции.
        '''
        self.log.debug(f'Called with args: ({tzid}, {message_to_code}, {msg_list}, {clean})')
        resp = await self._get(
            'getState', tzid=tzid, message_to_code=message_to_code,
            msg_list=msg_list, clean=clean
        )
        return [State(**r) for r in resp]

    async def set_operation_revise(self, tzid: int) -> int:
        '''Создает запрос на уточнение ответа по операции. Следует использовать, если поступил неверный код.
        Данный метод отправляет запрос на другой код в случае, если поступило несколько СМС на один номер с разными кодами.

        Args:
            tzid (int): Идентификатор операции.

        Returns:
            int: Идентификатор операции (tzid).
        '''
        self.log.debug(f'Called with args: ({tzid})')
        resp = await self._get('setOperationRevise', tzid=tzid)
        if resp.get('response', '-1') == 1:
            return resp.get('tzid', -1)
        else:
            raise APIError(resp.get('response', 'UnexpectedError'))

    async def set_operation_ok(self, tzid: int) -> Literal[True]:
        '''Отправляет уведомление об успешном получении кода и завершает операцию.

        Args:
            tzid (int): Идентификатор операции.

        Returns:
            Literal[True]: Операция закрыта.
        '''
        self.log.debug(f'Called with args: ({tzid})')
        resp = await self._get('setOperationOk', tzid=tzid)
        if resp.get('response', '-1') == 1:
            return True
        else:
            raise APIError(resp.get('response', 'UnexpectedError'))
