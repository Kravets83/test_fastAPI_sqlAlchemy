'''create base'''

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Устанавливаем соединение с postgres
connection = psycopg2.connect(user="postgres", password="postgres")
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создаем курсор для выполнения операций с базой данных
cursor = connection.cursor()
sql_create_database = r'C:\pythonProject12'
# Создаем базу данных
cursor.execute('create database sqlalchemy_APP2')
print(cursor())
# Закрываем соединение
cursor.close()
connection.close()
