from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
# Создаёт базовый класс, от которого наследуются все модели. Этот класс содержит информацию о метаданных базы данных.
# Это точка отсчёта для всех моделей. Без него SQLAlchemy не сможет определить, как связать ваши модели с таблицами в
# базе данных.

# Модель User
class User(Base):
    __tablename__ = 'users'  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True, autoincrement=True)  # Автоматически увеличивающийся первичный ключ
    name = Column(String, nullable=False)  # Обязательное текстовое поле
    email = Column(String, unique=True, nullable=False)  # Уникальное текстовое поле
    #age = Column(Integer, nullable=True)  # Новое поле
