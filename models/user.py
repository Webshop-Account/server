from typing import List

from pydantic import BaseModel, ConfigDict, constr
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic_extra_types.payment import PaymentCardNumber

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# создаем базовый класс для моделей
Base = declarative_base()

# создаем модель, объекты которой будут храниться в бд
class UserOrm(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    second_name = Column(String, )
    loging = Column(String, unique=True)
    password = Column(String, )
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    card_number = Column(String, )
class UserModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    second_name: str
    loging: str
    password: str
    phone: PhoneNumber
    email: str
    card_number: PaymentCardNumber
# создаем таблицы
Base.metadata.create_all(bind=engine)