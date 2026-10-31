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
- Docker

## 📋 Requirements

- Python 3.14
- A running PostgreSQL server and a database for the bot

## 🚀 Installation

```bash
git clone https://github.com/EmilN2S/task-manager-bot.git
cd task-manager-bot
```

With uv:

```bash
uv sync
```

Or with pip:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## ⚙️ Configuration

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
DATABASE_URL=postgresql://user:password@localhost:5432/tasksdb
```

Get a token from [@BotFather](https://t.me/BotFather). `DATABASE_URL` points to your PostgreSQL database; create the database first (for example with `createdb tasksdb`).

## ▶️ Usage

```bash
uv run python src/main.py
# or, without uv:
python src/main.py
```

Then open your bot in Telegram and send `/start`.

## 🐳 Docker

```bash
docker build -t task-manager-bot .
docker run -d --env-file .env task-manager-bot
```

The container needs network access to your PostgreSQL server, so make sure `DATABASE_URL` in `.env` uses a host that is reachable from inside the container (not `localhost`, unless you run it with `--network host`). Task data lives in PostgreSQL, so no volume is needed for the bot itself.

## 📁 Project structure

```
task-manager-bot/
├── Dockerfile
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