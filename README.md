# Учебный проект API для Yatube

API для проекта Yatube использует фреймворки Django и DRF, использует JWT-токены для аутентификации.
Формат передачи данных - JSON.
У неаутентифицированных пользователей доступ к API только на чтение.
Используются версия Python 3.7

## Как запустить проект:

Создать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры API запросов:

### Получить JWT-токен - http://127.0.0.1:8000/api/v1/token/

POST request:

```
{
  "username": "string",
  "password": "string"
}
```

Response:

```
{
  "access": "string",
  "refresh": "string"
}
```


### Обновить JWT-токен - http://127.0.0.1:8000/api/v1/token/refresh/

POST request:

```
{
  "refresh": "string"
}
```

Response:

```
{
  "refresh": "string"
}
```


### Получить список всех публикаций/Создать новую - http://127.0.0.1:8000/api/v1/posts/

POST Request:

```
{
  "text": "string"
}
```

Response:

```
[
  {
    "id": 0,
    "text": "string",
    "author": "string",
    "pub_date": "2019-08-24T14:15:22Z"
  }
]
```


### Получить/обновить/удалить публикацию по id http://127.0.0.1:8000/api/v1/posts/{id}/

PUT request:

```
{
  "text": "string"
}
```

Response:

```
{
  "id": 0,
  "text": "string",
  "author": "string",
  "pub_date": "2019-08-24T14:15:22Z"
}
```

