# Сервис полезных привычек

### Функционал 

CRUD-операции для привычек через API. 
Связь между привычками и пользователями. 
Настроены права доступа к функционалу по владельцу привычки. 
Настроена пагинация. 
Настроена асинхронная рассылка в телеграм 
пользователям о привычках с помощью Celery. 
Написаны тесты.

### Использование

* клонируйте репозиторий 
* инициализируйте poetry
* установите зависимости
* измените файл `.env_sample` и сохраните как `.env`
* примените миграции
* запустите сервер




### Эндпоинты

    Регистрация.
    Авторизация.
    Список привычек текущего пользователя с пагинацией.
    Список публичных привычек.
    Создание привычки.
    Редактирование привычки.
    Удаление привычки

http://localhost:8000/users/users/login/ 

метод POST

{"email":"1@habbit.ru",
"password":"123456789"}
получение токена

http://localhost:8000/users/users/

метод POST

{"email":"2@habbit.ru",
"username":"2user",
"password":"123456789"}

создание пользователя

http://127.0.0.1:8000/habits/list/

метод GET

Список привычек текущего пользователя с пагинацией

http://127.0.0.1:8000/habits/published/

метод GET

Список публичных привычек



### Использование API

Привычка (/habits/):

GET /habits/list/ — Получение списка привычек.

POST /habits/create/ — Создание нового привычек.

GET /habits/{id}/detail — Получение информации об привычке.

PUT /habits/{id}/update/ — Полное обновление привычки.

PATCH /habits/{id}/update/ — Частичное обновление привычки.

DELETE /habits/{id}/delete/ — Удаление привычки.

