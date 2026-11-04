# TaskFlow API

A multi-user task management API built with FastAPI and PostgreSQL.

## Tech stack
FastAPI · PostgreSQL · SQLAlchemy · Alembic · Pytest · uv · Docker

## Getting started
```bash
uv sync
cp .env.example .env
```

## Run the API
```bash
uv run uvicorn app.main:app --reload
```
Then open http://127.0.0.1:8000/docs


## Roadmap
- [x] Sprint 0: Project setup
- [ ] Sprint 1: FastAPI foundation
- [ ] Sprint 2: PostgreSQL and SQLAlchemy
- [ ] Sprint 3: Task CRUD and validation
- [ ] Sprint 4: Authentication
- [ ] Sprint 5: Authorization and ownership
- [ ] Sprint 6: Pagination, filtering and sorting
- [ ] Sprint 7: Testing, logging and errors
- [ ] Sprint 8: Docker, CI and release
