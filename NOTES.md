# Backend Playbook: TaskFlow API

## Sprint 0: Project setup
Goal: a safe, reproducible project before any app code.

---

### Subtask I: Create the repo and clone it
Created the repo on GitHub and cloned it locally. GitHub keeps the code backed up, and it's where reviews and CI will happen later.

---

### Subtask II: Set up Python with uv
- Pinned Python 3.13 (`.python-version`)
- `pyproject.toml`: what the project needs
- `uv.lock`: the exact versions resolved
- `.venv`: private packages, never committed

This makes the same setup work on every machine. Run with `uv run`, install with `uv add`.

---

### Subtask III: Add `.gitignore` and `.env.example`
- Ignore `.venv`, caches and `.env` (real secrets)
- Commit `.env.example` with fake values

Other people can see which settings are needed without ever seeing real secrets, because a secret pushed once stays in Git history forever.

---

### Subtask IV: Add the skeleton, README and NOTES
- `app/` and `tests/` with `__init__.py`, which make them Python packages
- README explains the project
- NOTES is this playbook

The project now has a clear structure and a first page that tells anyone what it is.

---

### Subtask V: Branch → PR → merge → protect `main`
- One branch per sprint, one commit per subtask
- PR with What / Why / How to test; read the diff, then merge
- `protect-main` ruleset blocks direct pushes

Every change gets reviewed, and the rule on GitHub holds even when I forget the habit.

---


## Sprint 1: FastAPI foundation
Goal: a running API with one route, a health check, docs and config.

---

### Subtask I: First FastAPI app
- `uv add "fastapi[standard]"` installs FastAPI and Uvicorn
- `app = FastAPI()` creates the app; `@app.get("/")` binds GET / to a function
- A returned dict becomes a JSON response automatically

This proved the full cycle: request → Uvicorn → FastAPI → function → JSON response.

---

### Subtask II: Health endpoint in its own router
- `APIRouter` in `app/api/routes/health.py`, plugged in with `app.include_router`
- `GET /health` returns `{"status": "ok"}`, with no database involved

Routes are grouped by feature in their own files, so `main.py` stays small. Monitors and Docker use `/health` to check the app is alive.

---

### Subtask III: Uvicorn and interactive docs
- `uv run uvicorn app.main:app --reload` (module `app/main.py`, variable `app`)
- `title`, `version` and `description` on `FastAPI(...)`
- `/openapi.json` is the contract; `/docs` (try it) and `/redoc` (read it) are views of it

This is the real startup command Docker will use, and the docs are generated from the code, so they never go stale.

---

### Subtask IV: Settings from the environment
- `Settings(BaseSettings)` in `app/core/config.py` reads `.env`
- Priority: real env var > `.env` > default
- `get_settings()` with `@lru_cache` builds settings once
- A required field with no default makes the app fail fast at startup

The same code runs everywhere, and only the environment changes (12-factor config). Secrets will never be in the code.

---

## Sprint 2: PostgreSQL and SQLAlchemy

