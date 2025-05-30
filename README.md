# Photo Loader

## О проекте

Тестовое задание. Приложение, позволяющее на главной странице просматривать таблицу с данными о загруженных файлах, API методом (POST) для загрузки изображения (в кодировке base64), а так же с возможностью тестирования 100 загрузок одного выбранного файла (они автоматом появятся через 20 секунд, но пользователь сможет продолжить работу на сайте сразу же). На главной странице открывается вебсокет, поэтому таблица при добавлении новых файлов обновляется автоматически. API POST метод для загрузки реализован в двух видах: я не совсем понял, нужно ли через 20 секунд дать ответ или дать ответ сразу и симитировать 20 секундную обработку. Сделал оба варианта на всякий:)


## Стек технологий
- Python 3
- Django 5
- Django Rest Framework
- PostgreSQL
- Docker
- Daphne
- Nginx
- Celery
- Redis (message broker and result backend)
- WebSocket
- Redoc


## Едпоинты
- POST /api/load_photo/
- POST /api/add_photo/

Два вышеуказанных ендпоинта - это разные виды решения одного и того же

- /admin
- /schema/
- /schema/redoc/

Подробное описание методов можно посмотреть в redoc после запуска проекта (127.0.0.1/schema/redoc/).

## Запуск проекта
- Клонируем репозиторий
```
git clone git@github.com:Okhnovsky/photo_loader.git
```
- Переходим в появившуюся директорию rphoto_loader/
```
cd photo_loader
```
- В данной директории создаем файл .env со следующими переменными:
```
SECRET_KEY=<>
DB_NAME=<>
POSTGRES_USER=<>
POSTGRES_PASSWORD=<>
DB_HOST=<>
DB_PORT=<>
CELERY_BROKER_URL=<>
```
- Запускаем контейнеры docker compose
```
docker compose up -d
```
- Применяем миграции, создаем суперпользователя, собираем статику:
```
docker compose exec app_backend python manage.py migrate
docker compose exec app_backend python manage.py createsuperuser
```
- Запускаем celery воркер в контейнере app_backend:
```
docker compose exec app_backend celery -A app worker -l INFO --detach
```
- Переходим в административную панель http://127.0.0.1/admin/
- Или сразу на главную: http://127.0.0.1/