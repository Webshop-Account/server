import sqlite3
from models.user import User


def select_user_data(user_id: int) -> User:
    sql_req: str = f"""select * from users where id={user_id}"""
