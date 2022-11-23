from dataclasses import dataclass
from typing import Any

@dataclass
class DatabaseConfig:
    db_host: str      #URL-адрес базы данных
    db_user: str      #Username пользователя базы данных
    db_password: Any  #Пароль к базе данных
    database: str     #Название базы данных


@dataclass
class TgBot:
    token: str            #Токен для доступа к телеграм-боту
    admin_ids: list  #Список id администраторов бота


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

#То есть, например, получить токен бота можно, будет так:

#А пароль к базе данных так:


MyDB = DatabaseConfig('URL-адрес', 'Vova', 'qwerty', 'MyDatabase')
MyTgBot = TgBot('token1234', [1, 2, 3, 4])
MyConfig = Config(MyTgBot, MyDB)

print(MyDB.__annotations__)

BOT_TOKEN = MyConfig.tg_bot.token
BD_PASSWORD = MyConfig.db.db_password

print(BOT_TOKEN, BD_PASSWORD)
