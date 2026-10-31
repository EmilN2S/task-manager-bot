# 📝 task-manager-bot

A Telegram bot for managing your daily tasks right inside the chat. Create tasks with priorities and deadlines, track statuses and clean up what's done, all with inline buttons.

<p>
<img src="https://img.shields.io/github/v/tag/EmilN2S/task-manager-bot" alt="Version">
<img src="https://img.shields.io/github/license/EmilN2S/task-manager-bot" alt="License">
<img src="https://img.shields.io/github/last-commit/EmilN2S/task-manager-bot" alt="Last commit">
</p>

## ✨ Features

- Create tasks with a title, description, priority and deadline
- View your task list with priority, deadline and completion status
- Change task status (mark a task as finished by its ID)
- Delete tasks by ID
- Navigation through inline keyboard buttons, no need to remember commands
- Built-in Help, FAQ and Privacy sections

## 🛠 Tech stack

- Python 3.14
- [aiogram 3](https://docs.aiogram.dev/) for the Telegram bot
- PostgreSQL via [asyncpg](https://github.com/MagicStack/asyncpg)
- python-dotenv for configuration
- [uv](https://docs.astral.sh/uv/) for dependency management
- Docker and Docker Compose

> **Note:** the bot only contains the PostgreSQL *client* (asyncpg). The PostgreSQL *server* is a separate program: the Docker Compose setup below starts it for you, and for a local run you need your own.

## ⚙️ Configuration

Get a bot token from [@BotFather](https://t.me/BotFather), then create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql://user:password@localhost:5432/tasksdb
```

`DATABASE_URL` format: `postgresql://USER:PASSWORD@HOST:PORT/DATABASE`.

## 🐳 Quick start with Docker Compose (recommended)

Requires Docker with the Compose plugin. This starts both PostgreSQL and the bot.

```bash
git clone https://github.com/EmilN2S/task-manager-bot.git
cd task-manager-bot
# create .env with BOT_TOKEN (see Configuration)
docker compose up -d --build
```

Useful commands:

```bash
docker compose logs -f bot    # watch the bot logs
docker compose ps             # check that both services are running
docker compose down           # stop everything (data is kept)
docker compose down -v        # stop everything AND delete the database
```

Compose sets the database host to `db` for the bot automatically, so the `localhost` value in `.env` is ignored here. Tasks are stored in the `pgdata` volume and survive restarts and rebuilds. The default database credentials are in `docker-compose.yml`, so change them before exposing the database outside your machine.

Then open your bot in Telegram and send `/start`.

## 💻 Run locally without Docker

You need Python 3.14 and a running PostgreSQL server.

1. Create the database, for example:

   ```bash
   sudo -u postgres psql -c "CREATE USER bot WITH PASSWORD 'secret';"
   sudo -u postgres psql -c "CREATE DATABASE tasksdb OWNER bot;"
   ```

2. Set `DATABASE_URL` in `.env` to match, e.g. `postgresql://bot:secret@localhost:5432/tasksdb`.

3. Install dependencies and start the bot.

   With uv:

   ```bash
   uv sync
   uv run python src/main.py
   ```

   Or with pip:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python src/main.py
   ```

Then open your bot in Telegram and send `/start`.

## 🔧 Troubleshooting

- **`connection refused` or the bot can't reach the database:** in Docker the host must be `db` (Compose handles this), not `localhost`. Locally, check that PostgreSQL is running.
- **`password authentication failed`:** the user and password in `DATABASE_URL` must match your PostgreSQL user, or the values in `docker-compose.yml`. If you changed them after the first start, run `docker compose down -v` once, because the old credentials are stored in the volume.
- **Build is slow or huge:** make sure `.dockerignore` exists, so `.venv` and `.git` are not copied into the image.

## 📁 Project structure

```
task-manager-bot/
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── uv.lock
└── src/
    ├── main.py          # entry point
    ├── utils.py         # helpers (priority and status to text)
    ├── database/        # PostgreSQL access via asyncpg (pgdb.py)
    ├── handlers/        # start, help, faq, privacy, create/list/delete tasks, task status
    ├── keyboards/       # inline keyboards (main menu, help, priority, status, delete)
    └── states/          # FSM states for task creation, deletion and priority
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).