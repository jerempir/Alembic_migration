from sqlalchemy.orm import sessionmaker
from models import  User
from config import engine
# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

# Добавляем возраст пользователю Alice
user = session.query(User).filter_by(name="Alice").first()
user.age = 30
session.commit()

# Читаем данные снова
users = session.query(User).all()
for user in users:
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}, Age: {user.age}")
