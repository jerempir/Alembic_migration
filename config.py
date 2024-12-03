
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "jerem"
DB_HOST = "localhost"
DB_NAME = "TechnoSchool"

# Формируем URL из переменных
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Создаем движок
engine = create_engine(DATABASE_URL)

print("Подключение успешно настроено!")
