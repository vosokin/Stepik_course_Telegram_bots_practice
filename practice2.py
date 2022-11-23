from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    name: str
    age: int
    email: str

man = User(346, 'Vova', 36, 'vova@mail.ru')
print(man.name)