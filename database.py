import sqlite3
import logging
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("students.db") #Подключение к бд, если такого файла нет, он сам создается

logging.info("Соединение с базой данных установлено")

cur = connection.cursor() #Создание "курсора(?)" с которым будем работать
cur.execute(""" 
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT,
    age INTEGER
);
""")
#primary key делает айди уникальным, которое никогда не повториться, autoincrement заполняет id самостотельно

# try:
#     cur.execute("INSERT INTO students (name,age) VALUES ('Bob', 14);")
#     cur.execute("INSERT INTO students (name,age) VALUES ('Nigg', 17);")
#     cur.execute("INSERT INTO students (name,age) VALUES ('Megafon', 2);")
#     cur.execute("INSERT INTO students (name,age) VALUES ('Bomba', 23);")
#     cur.execute("INSERT INTO students (name,age) VALUES ('Er', 7);")  # execute выполняет SQL запрос
#     logging.info("SQL Запрос успешно выполнен, проверьте базу данных")
#     #Каждый раз когда будем запускать код, оно будет выполняться и заполнятся ещё раз, так что лучще закомментировать/создать другой файл
#
# except:
#     logging.error("Произошла неизвестная ошибка при выполнении SQL запроса, попробуйте ещё раз")

#Читаем данные
cur.execute("SELECT * FROM students;")

students = cur.fetchall() #извлечь всё

for student in students:
    print(student)

cur.execute("UPDATE students SET age = 16 WHERE name = 'Bob';")
logging.info("Для записей с именем Боб изменен возраст на 16")

#CRUD. Create. Read. Update. Delete.

connection.commit() #Мы говорим что берём курсор (слепок(?)) и сохраняем
connection.close()