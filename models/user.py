from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber

class User(BaseModel):
    id: int
    first_name: str
    second_name: str
    loging: str
    password: str
    phone: PhoneNumber
    email: str