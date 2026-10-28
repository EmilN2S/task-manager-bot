import asyncpg
from os import getenv
from dotenv import load_dotenv
import datetime
from asyncio import run

load_dotenv()

DATABASE_URL = getenv("DATABASE_URL")

async def main():
    conn = await asyncpg.connect(DATABASE_URL)

    await conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_id INT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT FALSE,
            priority BOOLEAN DEFAULT FALSE,
            deadline DATE
        )
    ''')

    await conn.execute('''
        INSERT INTO users(name, dob) VALUES($1, $2)
    ''', 'Bob', datetime.date(1984, 3, 1))

    # Select a row from the table.
    row = await conn.fetchrow(
        'SELECT * FROM users WHERE name = $1', 'Bob')
    # *row* now contains
    # asyncpg.Record(id=1, name='Bob', dob=datetime.date(1984, 3, 1))
    print(row)
    # Close the connection.
    await conn.close()

run(main())