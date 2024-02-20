docker-compose exec superset bash
# Обновление схемы базы данных
superset db upgrade
# Инициализация Superset (если еще не выполнено)
superset init
# Создание административного пользователя
superset fab create-admin \
--username admin \
--firstname Superset \
--lastname Admin \
--email admin@superset.com \
--password admin