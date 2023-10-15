### Question bot

The bot allows people to send anonymous questions to other people.

### Technologies

- Python 3.11
- [Aiogram](https://github.com/aiogram/aiogram) - asynchronous framework for Telegram Bot API
- [arq](https://github.com/samuelcolvin/arq) - asynchronous task queue
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) - ORM with async support
- [Alembic](https://github.com/sqlalchemy/alembic) - migrations
- [Pillow](https://github.com/python-pillow/Pillow) - image processing
- PostgreSQL - main database
- Redis - save user state
- Docker - containerization
- Docker-compose - run all services

***
### Installation
1) Clone repository
```bash
git clone https://github.com/itisnotyourenv/questions-bot
```
2) Rename `.env.dist` to `.env` and fill in the variables
3) Run docker-compose
```bash
docker-compose up -d --build
```
4) Run migrations
```bash
docker exec q_bot alembic upgrade head
```
Where `q_bot` is the name of the container with the bot
