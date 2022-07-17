# [onlinesim.ru](https://onlinesim.ru) API
Библиотека для работы с API сайта [onlinesim.ru](https://onlinesim.ru)
Их документация доступна по [ссылке](https://onlinesim.ru/docs/api/ru/)
Есть синхронный и асинхронный клиент.

### Зачем если есть оффициальная библиотека?
Затем что оффициальная библиотека почему-то удалили поддержку async. А я вернул.

### Установка
Напрямую с помощью pip и git:
```sh
pip install git+https://github.com/LulzLoL231/pyOnlinesimRuAPI
```
Или из исходников:
```sh
git clone https://github.com/LulzLoL231/pyOnlinesimRuAPI
cd pyOnlinesimRuAPI
python3 setup.py install
```

### Пример получения баланса
```python
from asyncio import run

from onlinesim import OnlinesimRu
from onlinesim import AsyncOnlinesimRu


user = OnlinesimRu('%API_KEY%').user
bal = user.get_balance()  # onlinesim.schemas.Balance


async def get_active_operations():
    sms = AsyncOnlinesimRu('%API_KEY%').sms
    opers = await sms.get_state()
    return opers 

opers_len = len((run(get_active_operations())))

print(f'Ваш доступный баланс: {bal.balance} RUB')
print(f'На текущий момент выполняется {opers_len} операций.')
```
