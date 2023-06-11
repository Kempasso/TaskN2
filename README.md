# Questions microservice

### Описание:

Создание юзера, добавление аудиозаписи в базу данных.

### Требования:

* Python 3.10
* Docker/Compose

### Установка:

Сборка приложения

```bash
sudo docker-compose build
```

### Запуск приложения:

```bash
sudo docker-compose up
```

### Пример POST запроса - создание юзера (Полученные user_uuid и user_id нужны для добавления аудио)

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username": "gggdsasdadd"}' http://127.0.0.1:8000/api/user/
```

### Полученные user_uuid и user_id вписать в поля YOUR_UUID и YOUR_USER_ID

```bash
curl -X POST -H "Content-Type: multipart/form-data" \
-F "file=@files/1.wav" \
-F "user_uuid=YOUR_UUID" \
-F "user_id=YOUR_USER_ID" \
http://127.0.0.1:8000/api/record/
```

### Коннект к базе данных

```bash
docker-compose exec db psql -U postgres -d Task2
```