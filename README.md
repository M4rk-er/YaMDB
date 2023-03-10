# YaMDB API              ![CI](https://github.com/M4rk-er/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. В каждой категории есть произведения: книги, фильмы или музыка. Произведению может быть присвоен жанр из списка предустановленных. Новые жанры может создавать только администратор. Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы и ставят произведению оценку в диапазоне от одного до десяти; из пользовательских оценок формируется усреднённая оценка произведения — рейтинг. На одно произведение пользователь может оставить только один отзыв.

#### Если Docker не установлен, перейдите на [официальный сайт ](https://www.docker.com/products/docker-desktop) и скачайте установочный файл Docker Desktop для вашей операционной системы

### Клонировать репрозиторий:
```
git@github.com:M4rk-er/yamdb_final.git
``` 

### После клонирования репрозитория:

- Перейдите в директорию infra
``` 
cd infra 
```
- Создать файл ``` .env ```

```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432 
```
- Собрать и запустить контейнеры:
``` 
docker-compose up -d --build 
```

- Выполнить миграции:
``` 
docker-compose exec web python manage.py migrate 
```

- Создать суперпользователя:
``` 
docker-compose exec web python3 manage.py createsuperuser 
```

- Собрать staticfiles:
``` 
docker-compose exec web python3 manage.py collectstatic --noinput 
```

### После запуска проект будет доступен по адресу localhost, [документация](localhost/redoc/), [панель администратора](localhost/admin/)

### Пользовательские роли:
* Аноним — может просматривать описания произведений, читать отзывы и комментарии.
* Аутентифицированный пользователь (user) — может читать всё, как и Аноним, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.
* Модератор (moderator) — те же права, что и у Аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
* Администратор (admin) — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
* Суперюзер Django - обладает правами администратора (admin) 
>
### Регистрация нового пользователя:
```(POST) /api/v1/auth/signup/```
#### На email приходит confirmation_code для получения JWT-Token
```
{ 
    "email": "string",
    "username": "string"
}
```
>
### Получение JWT-token:
```(POST) /api/v1/auth/token/```
```
{
    "username": "string",
    "confirmation_code": "string"
}
```
### Более подробная документация со всеми адресами и доступными методами доступны по ссылкам, указанным ниже:
>
### Динамическая документация Swagger - [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
>
### Спецификация ReDoc - [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

## Использованные технологии/пакеты
* Python 3.7
* Django 2.2.16
* PyJWT 2.1.0
* django-filter 2.4.0
* djangorestframework 3.12.4
* djangorestframework-simplejwt 4.7.2
* drf-yasg 1.21.3
* requests 2.26.0

## Групповой проекта выполенен командой №21 коготры №41 курса "Backend developer"
* [Артем  Зимин](https://github.com/G1lza92)
* [Сергей Гриценко (team lead)](https://github.com/GritsenkoSerge/)
* [Марк Британов](https://github.com/M4rk-er)
### под руководством
* Олег Портнихин (наставник)
* Андрей Квичанский (ревьюер)
