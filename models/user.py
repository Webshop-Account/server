from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from pydantic_extra_types.payment import PaymentCardNumber

class User(BaseModel):
    id: int
    first_name: str
    second_name: str
    loging: str
    password: str
    phone: PhoneNumber
    email: str
    number: PaymentCardNumber