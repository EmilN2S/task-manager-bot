import asyncpg

pool = None

async def init_db(url):
    global pool

    pool = await asyncpg.create_pool(url)

    await pool.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_id BIGINT NOT NULL,
            title TEXT NOT NULL,
            description TEXT,
            task_status BOOLEAN DEFAULT FALSE,
            priority BOOLEAN DEFAULT FALSE,
            deadline DATE
        )
    ''')

async def close_db():
    await pool.close()

async def add_tasks(user_id, title, description, priority, deadline):
    await pool.execute('''
        INSERT INTO tasks(user_id, title, description, priority, deadline)
        VALUES($1, $2, $3, $4, $5)
    ''', user_id, title, description, priority, deadline)

async def get_tasks(user_id):
    rows = await pool.fetch('''
        SELECT task_id, title, description, task_status, priority, deadline 
        FROM tasks WHERE user_id = $1''', user_id)
    return rows

async def get_tasks_lite(user_id):
    rows = await pool.fetch('''
        SELECT task_id, title 
        FROM tasks WHERE user_id = $1''', user_id)
    return rows

async def delete_task(task_id, user_id):
    await pool.execute('DELETE FROM tasks WHERE task_id = $1 AND user_id = $2', task_id, user_id)