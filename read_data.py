
from sqlalchemy.orm import sessionmaker
from models import User
from config import engine  # Импорт движка из config.py

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Читаем данные
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
