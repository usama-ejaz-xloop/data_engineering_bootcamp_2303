from typing import List

import psycopg2

import config


connection = psycopg2.connect(config.DB_CONNECTION_STRING)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS todo(content TEXT)")
connection.commit()
cursor.execute("CREATE TABLE IF NOT EXISTS secrets(secret TEXT)")
cursor.execute(
    "INSERT INTO secrets(secret) VALUES ('FLAG{SQL_injection_allows_to_read_arbitrary_data_from_the_database_and_sometimes_modify_it}')"
)
connection.commit()


def add_todo_item(content: str) -> None:
    connection = psycopg2.connect(config.DB_CONNECTION_STRING)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO todo(content) VALUES(%s)", (content,))
    connection.commit()


def list_todo_items(containing_string: str) -> List[str]:
    connection = psycopg2.connect(config.DB_CONNECTION_STRING)
    cursor = connection.cursor()
    cursor.execute(
        f"SELECT content FROM todo WHERE content LIKE '%{containing_string}%'"
    )

    result = []
    for item in cursor.fetchall():
        result.append(item[0])

    return result
