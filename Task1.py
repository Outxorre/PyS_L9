import sqlite3
import logging
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect("books.db")

logging.info("Соединение с базой данных установлено")

cur = connection.cursor()
cur.execute(""" 
CREATE TABLE IF NOT EXISTS books(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    title TEXT,
    author TEXT
);
""")



cur.execute("INSERT INTO books (title,author) VALUES ('Biba', 'Vobla99');")
cur.execute("INSERT INTO books (title,author) VALUES ('Boba', 'Abilaykhan');")
cur.execute("INSERT INTO books (title,author) VALUES ('Megafon', 'Arlan');")
logging.info("SQL Запрос успешно выполнен, проверьте базу данных")



try:
    cur.execute("SELECT * FROM books;")

    students = cur.fetchall()

    for student in students:
        print(student)
    logging.info("Успешный вывод")

except:
    "Unknown error"