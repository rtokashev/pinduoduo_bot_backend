### Генерация миграций

```bash
PYTHONPATH=src alembic revision --autogenerate -m "общее_описание_миграции"
```

### Запуск postgres-а локально
Пункт актуален, пока весь процесс настройки pg не будет настроен на развертку простым compose up.

1. Запуск pg локально(без миграций и триггеров, крон джобы создаются при запуске)
    ```bash
    docker-compose -f docker-compose.local.yaml --build up -d
    ```
2. Накатывание миграции до актуального состояния
    ```bash
    PYTHONPATH=src alembic upgrade head
    ```
3. Далее чтобы воспроизводилось полное поведение всей планируемой бизнес-логики, необходимо создать триггеры.
   Можно перейти в dbeaver или pgadmin в базу и там исполнить содержимое скрипта postgres/scripts/triggers.sql
   либо запустить команду: 
   ```bash
   psql -h 0.0.0.0 -U postgres -d postgres -a -f postgres/scripts/triggers.sql
   ```