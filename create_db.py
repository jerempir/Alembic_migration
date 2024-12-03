
from models import Base
from config import engine  # Импорт движка из config.py

# Создаем таблицы
Base.metadata.create_all(engine)
print("База данных создана!")
