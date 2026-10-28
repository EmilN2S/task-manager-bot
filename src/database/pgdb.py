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
        CREATE TABLE users(
            id serial PRIMARY KEY,
            name text,
            dob date
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

    # Close the connection.
    await conn.close()

run(main())