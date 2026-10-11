# 📝 task-manager-bot

A Telegram bot for managing your daily tasks right inside the chat. Create tasks, set priorities, track statuses and clean up what's done, all with inline buttons.

<p>
  <img src="https://img.shields.io/github/v/tag/EmilN2S/task-manager-bot" alt="Version">
  <img src="https://img.shields.io/github/license/EmilN2S/task-manager-bot" alt="License">
  <img src="https://img.shields.io/github/last-commit/EmilN2S/task-manager-bot" alt="Last commit">
</p>

## ✨ Features

- Create tasks with a priority
- View your task list
- Change task status
- Delete tasks
- Navigation through inline keyboard buttons, no need to remember commands
- Built-in Help, FAQ and Privacy sections

## 🚧 Roadmap

- [ ] Task deadlines (planned after the main release)

## 🛠 Tech stack

- Python 3.14
- [aiogram 3](https://docs.aiogram.dev/) for the Telegram bot
- SQLite via [aiosqlite](https://github.com/omnilib/aiosqlite)
- python-dotenv for configuration
- [uv](https://docs.astral.sh/uv/) for dependency management
- Docker

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
```

Get a token from [@BotFather](https://t.me/BotFather).

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
docker run -d --env-file .env \
  -v task-manager-data:/app/src/database/data \
  task-manager-bot
```

The volume keeps `tasks.db` between container restarts.

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
    ├── database/        # SQLite access (db.py) and data/ with tasks.db
    ├── handlers/        # start, help, faq, privacy, create/list/delete tasks, task status
    ├── keyboards/       # inline keyboards (main menu, help, priority, status, delete)
    └── states/          # FSM states for task creation, deletion and priority
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).
