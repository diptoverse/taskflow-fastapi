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

### Retro
The ruleset said "created" but had no target, so it protected nothing. Test safety rules; don't assume they work.

---

## Sprint 1: FastAPI foundation
