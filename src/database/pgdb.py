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
            task_status BOOLEAN DEFAULT FALSE,
            priority BOOLEAN DEFAULT FALSE,
            deadline DATE
        )
    ''')

    row = await conn.fetchrow(
        'SELECT * FROM tasks')

    print(row)

    await conn.close()

async def add_tasks(user_id, title, description, priority, deadline):
    await conn.execute('''
        INSERT INTO tasks(user_id, title, description, priority, deadline) VALUES($1, $2, $3, $4, $5)
    ''', user_id, title, description, priority, datetime.date(deadline))
    

run(main())