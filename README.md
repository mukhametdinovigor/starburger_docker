# Сайт доставки еды Star Burger

[Перейти на сайт](http://mhnsite.ru/)

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом.

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)


Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит менеджер, чтобы обновить меню ресторанов Star Burger.


## Запуск dev окружения

Скачать код с `github`

Создать файл `.env` в папке `star-burger`:

- `DEBUG` — дебаг-режим. Поставьте `True`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте. Не стоит использовать значение по-умолчанию, **замените на своё**.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `YANDEX_GEOCODE_APIKEY` - API Яндекс-геокодера. Для получения координат места.
                            Получите API ключ в [кабинете разработчика](https://developer.tech.yandex.ru/services/)
- `ROLLBAR_TOKEN` - токен для системы логирования ROLLBAR [Сайт ROLLBAR](https://rollbar.com/)
- `ROLLBAR_ENVIRONMENT` - настройка environment в Rollbar, задайте свое значение например `your_name_dev`
- `DATABASE_URL` - настройка БД, для postgres выглядит так: `postgres://USER:PASSWORD@HOST:PORT/NAME`


Запустить `docker-compose`

```
docker-compose -f docker-compose.dev.yml up
```

Затем на новой вкладке создать миграции в БД

```
docker-compose -f docker-compose.dev.yml exec web python star-burger/manage.py migrate
```



## Запуск prod окружения

Скачать код с `github`

Создать файл `.env` в папке `star-burger`:

- `DEBUG` — дебаг-режим. Поставьте `False`.
- `SECRET_KEY` — секретный ключ проекта. Он отвечает за шифрование на сайте. Например, им зашифрованы все пароли на вашем сайте. Не стоит использовать значение по-умолчанию, **замените на своё**.
- `ALLOWED_HOSTS` — [см. документацию Django](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `YANDEX_GEOCODE_APIKEY` - API Яндекс-геокодера. Для получения координат места.
                            Получите API ключ в [кабинете разработчика](https://developer.tech.yandex.ru/services/)
- `ROLLBAR_TOKEN` - токен для системы логирования ROLLBAR [Сайт ROLLBAR](https://rollbar.com/)
- `ROLLBAR_ENVIRONMENT` - настройка environment в Rollbar, задайте свое значение например `your_name_prod`
- `DATABASE_URL` - настройка БД, для postgres выглядит так: `postgres://USER:PASSWORD@HOST:PORT/NAME`

Запустить скрипт

```
./prod_env.sh
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).
