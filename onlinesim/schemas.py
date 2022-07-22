# -*- coding: utf-8 -*-
#
#  Onlinesim API: Schemas.
#  Created by LulzLoL231 at 17/7/22
#
from typing import Dict
from decimal import Decimal

from pydantic import BaseModel, validator


class Balance(BaseModel):
    balance: Decimal
    zbalance: Decimal


class NumbersStatsService(BaseModel):
    count: int
    popular: bool
    price: Decimal
    id: int
    service: str
    slug: str


class NumbersStats(BaseModel):
    name: str
    position: int
    code: int
    new: bool
    enabled: bool
    services: Dict[str, NumbersStatsService]


class GetNumberResponse(BaseModel):
    tzid: int
    number: str | None

    @validator('number')
    def get_number_wo_plus(cls, number: str) -> str:
        return number.replace('+', '')


class State(BaseModel):
    tzid: int
    service: str
    number: str
    msg: str | None
    time: str
    form: str
    forward_status: int | None
    forward_number: str | None
    country: int
