### API для проекта Yatube

API для проекта Yatube использует фреймворки Django и DRF, использует JWT-токены для аутентификации.
У нуаутентифицированных пользователей доступ к API только на чтение.
Используются версия Python 3.7

## Как запустить проект:

Соиздать и активировать виртуальное окружение:

'''
python3 -m venv venv
'''

'''
source venv/Scripts/activate
'''

Установить зависимости из файла requirements.txt:

'''
python -m pip install --upgrade pip
'''

'''
pip install -r requirements.txt
'''

Выполнить мингации:

'''
python manage.py migrate
'''

Запустить проект:

'''
python manage.py runserver
'''

Примеры API запросов приведены по адресу запущенного проекта - http://127.0.0.1:8000/redoc/
