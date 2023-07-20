from pydantic import BaseModel

class Order(BaseModel):
    # identification of order
    id: int
    # identification of customer
    user_id: int
    # number of order in hall`s screen
    number: int
    # list of goods which user want to buy
    goods: list
    # total price of order
    total_cost: int


