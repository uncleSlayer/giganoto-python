import sqlite3

conn = sqlite3.connect("mydb.db")

cursor = conn.cursor()

# create table
cursor.execute(
    """
        CREATE TABLE users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        ) 
    """
)

# insert into table
cursor.execute(
    """
        INSERT INTO users(name, age)VALUES(?, ?)
    """,
    ("Siddhant", 23)
)

# show data from the table
cursor.execute(
    """
        SELECT * FROM users
    """
)

rows = cursor.fetchall()

for row in rows:
    print(row)

# insert multiple rows at once
pass_values = [('siddhant05', 223), ('morty07', 225), ('som', 55), ('shanu', 2223055787)]

cursor.executemany(
    """
        INSERT INTO users(name, age)VALUES(?, ?)
    """,
    pass_values
)

# update row
cursor.execute(
    """
        UPDATE users SET name = ? WHERE id = ?
    """,
    ('mohan', 2)
)

# delete a row
cursor.execute(
    """
        DELETE FROM users WHERE id = ? 
    """,
    (2,)
)

# drop the table
cursor.execute(
    """
        DROP TABLE users
    """
)

conn.commit()