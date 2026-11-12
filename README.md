# AI-Platform

A single platform that hosts multiple AI applications in one standard folder structure.

## Quick start

```bash
# 1. Install uv (https://docs.astral.sh/uv/)
pip install uv

# 2. Install dependencies
uv sync

# 3. Copy the environment template and fill in real values
cp .env.example .env

# 4. Run the platform
uv run python main.py          # lists available apps
uv run python main.py app1     # runs App1

# 5. Run tests
uv run pytest
```

## Folder structure

| Folder / File | Description |
|---|---|
| `main.py` | Starting point of the platform. Launches the selected apps. |
| `Apps/` | All AI applications. Each app has its own folder. |
| `core/` | Platform-wide foundations like settings, logging and errors. |
| `shared/` | Reusable parts used by more than one app. |
| `Tests/` | Platform-wide and cross-app tests. |
| `Data/` | Data files used in local development. |
| `docs/` | Platform documentation. |
| `Docker/` | Files to build and run containers. |
| `scripts/` | Reusable scripts for developers and maintenance. |
| `migrations/` | Database changes, if the platform owns the database. |
| `.github/workflows/` | CI/CD pipelines that test, build and deploy. |

The full folder guide is in `docs/standards/AI_Platform_Folder_Structure.pdf`.

## Adding a new app

1. Copy `Apps/App1/` to `Apps/<NewApp>/`.
2. Update its `README.md`, `pyproject.toml` and `.env.example`.
3. Register it in the `APPS` list in the root `main.py`.
