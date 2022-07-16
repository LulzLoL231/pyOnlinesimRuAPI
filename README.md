# [onlinesim.ru](https://onlinesim.ru) API
Библиотека для работы с API сайта [onlinesim.ru](https://onlinesim.ru)
Их документация доступна по [ссылке](https://onlinesim.ru/docs/api/ru/)

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
from onlinesim import UserAPI


user = UserAPI('%API_KEY%')
bal = await user.get_balance()  # onlinesim.user.Balance

print(f'Ваш доступный баланс: {bal.balance} RUB')
```
