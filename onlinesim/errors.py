# -*- coding: utf-8 -*-
#
#  Onlinesim API: Exceptions.
#  Created by LulzLoL231 at 7/7/22
#
class APIError(Exception):
    def __init__(self, error: str, text: str = None):
        errors = {
            "ACCOUNT_BLOCKED": "Аккаунт заблокирован",
            "ERROR_WRONG_KEY": "Неверный API ключ",
            "ERROR_NO_KEY": "Не указан API ключ",
            "ERROR_NO_SERVICE": "Не указан сервис",
            "REQUEST_NOT_FOUND": "Неизвестный API метод",
            "API_ACCESS_DISABLED": "API отключен в профиле",
            "API_ACCESS_IP": "Доступ к API с данного IP запрещён",
            "WARNING_NO_NUMS": "Нету совпадающих номеров",
            "TZ_INPOOL": "Ожидайте номер для присваивания к данной операции",
            "TZ_NUM_WAIT": "Ожидайте ответа",
            "TZ_NUM_ANSWER": "Ответ отправлен",
            "TZ_OVER_EMPTY": "Ответ не пришёл за отведённое время",
            "TZ_OVER_OK": "Операция выполнена",
            "ERROR_NO_TZID": "tzid не указан",
            "ERROR_NO_OPERATIONS": "Операций нету",
            "ACCOUNT_IDENTIFICATION_REQUIRED": "Необходимо пройти идентификацию: для заказа мессенджера - любым способом, для переадресации - по паспорту.",
            "EXCEEDED_CONCURRENT_OPERATIONS": "maximum quantity of numbers booked concurrently is exceeded for your account",
            "NO_NUMBER": "temporarily no numbers available for the selected service",
            "TIME_INTERVAL_ERROR": "delayed SMS reception is not possible at this interval of time",
            "INTERVAL_CONCURRENT_REQUESTS_ERROR": "maximum quantity of concurrent requests for number issue is exceeded, try again later",
            "TRY_AGAIN_LATER": "temporarily unable to perform the request",
            "NO_FORWARD_FOR_DEFFER": "forwarding can be activated only for online reception",
            "NO_NUMBER_FOR_FORWARD": "there are no numbers for forwarding",
            "ERROR_LENGTH_NUMBER_FOR_FORWARD": "wrong length of the number for forwarding",
            "DUPLICATE_OPERATION": "adding operations with identical parameters",
            "ERROR_NO_NUMBER": "number is not specified",
            "ERROR_PARAMS": "one or both parameters are wrong",
            "LIFICYCLE_NUM_EXPIRED": "the number has expired",
            "NEED_EXTENSION_NUMBER": "you have to extend the number, see the Extension tab",
            "ERROR_NUMBERS_PARAMS": "error in the number format",
            "ERROR_WRONG_TZID": "error in the number format",
            "NO_COMPLETE_TZID": "unable to complete the operation.",
            "NO_CONFIRM_FORWARD": "unable to confirm forwarding",
            "ERROR_NO_SERVICE_REPEAT": "no services for repeated reception",
            "SERVICE_TO_NUMBER_EMPTY": "no numbers for repeated reception for this service",
            'UnexpectedError': 'Неизвестная ошибка'
        }

        if not text and errors.get(error):
            raise APIError(error, errors.get(error))
        self.error = error
        self.text = text
