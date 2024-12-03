
from sqlalchemy.orm import sessionmaker
from models import User
from config import engine  # Импорт движка из config.py

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Добавляем данные
user1 = User(name="Alice", email="alice@example.com")
user2 = User(name="Bob", email="bob@example.com")

session.add(user1)
session.add(user2)
session.commit()

print("Данные добавлены!")
