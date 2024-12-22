# Микросервис для загрузки и просмотра информации о рабочих


## Содержание
- [Описание](#описание)
- [Технологии](#технологии)
- [Запуск проекта](#запуск-проекта)
- [Пример использования](#пример-использования)
- [Документация](#просмотр-документации)


## Описание
Микросервис реализует следующие методы:
- get .../api/v1/team/<team_id>/WorkerList - Возвращает список работников в бригаде
- get .../api/v1/worker/<worker_id> - Возвращает описание мастера
- put .../api/v1/r'^upload/(?P<filename>[^/]+)$' - Загружает файл excel и сохраняет данные работников в БД

## Технологии
- Python
- Django
- DRF
- PostgreSQL
- drf-yasg
- openpyxl


## Запуск проекта
1. Клонируйте проект
```
git clone git@github.com:aleksandrasilina/workers.git
```
2. Установите зависимости
```
pip install -r requirements.txt
```
3. Создайте файл .env в соответствии с шаблоном .env.sample
4. Примените миграции
```
python manage.py migrate
```
5. Запустите проект
```
python manage.py runserver
```

## Пример использования
Postman
1. Загрузка данных из /media/workers.xlsx и сохранение в БД:

PUT .../api/v1/upload/workers.xlsl

body -> form-data -> Key: file, Value: workers.xlsx

Response:
```
{
    "status": "success",
    "message": "File uploaded."
}
```
2. Просмотр списка работников в бригаде:
GET .../api/v1/team/2/WorkerList

Response:
```
[
    {
        "id": 2,
        "worker_id": 2,
        "name": "Петров",
        "team_id": 2,
        "salary": 120000,
        "specialization": "Черновая отделка"
    },
    {
        "id": 5,
        "worker_id": 5,
        "name": "Сергеев",
        "team_id": 2,
        "salary": 20000,
        "specialization": "Прораб"
    }
]
```

## Просмотр документации
http://127.0.0.1:8000/swagger/

http://127.0.0.1:8000/redoc/