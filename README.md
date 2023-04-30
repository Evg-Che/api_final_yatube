# api_final_yatube

### Описание: 
API для социальной сети Yatube.
API позволяет авторизованным пользователям создавать, просматривать, комментировать посты, подписываться на других пользователей.

### Как запустить проект:
Клонировать репозиторий:
```
git@github.com:Evg-Che/api_final_yatube.git
```
Перейти в каталог с проектом в командной строке:
```
cd yatube_api/
```
Cоздать и активировать виртуальное окружение:
(для Windows везде использовать python а не python3)
```
python3 -m venv env 
```
```
source env/bin/activate
```
Обносить pip и установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip 
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
    
Все доступные запросы можно посмотреть на http://127.0.0.1:8000/redoc/
### Технологии:
- Python 3.7
- Django 2.2.16
- djoser 2.1
- django rest framework
- Simple JWT

### Автор:
Евгения Че
