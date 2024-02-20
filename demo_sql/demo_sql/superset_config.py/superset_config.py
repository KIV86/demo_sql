SECRET_KEY = 'vrpndYv6PnTjl3E/cZz7NECZf8XNoX74qUn2aBtY7+C42HTugsbgN+wC'

# Строка подключения к базе данных для метаданных Superset
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@postgres/testdb'


# Настройки безопасности
SESSION_COOKIE_SAMESITE = 'Lax'  # Борьба с атаками CSRF
WTF_CSRF_ENABLED = True

# Настройки логирования
import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')
logging.getLogger().setLevel(logging.DEBUG)

# Настройки производительности
SUPERSET_WEBSERVER_WORKERS = 4  # Количество воркеров для Gunicorn
SUPERSET_WEBSERVER_TIMEOUT = 60  # Тайм-аут для веб-сервера