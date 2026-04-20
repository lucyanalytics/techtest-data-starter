# Lucy Tech Test — Starter

## What this is

The starter repository for Lucy Analytics' Junior Data/App Developer tech test. You'll build a small pipeline that ingests a messy CSV of hospitality POS transactions, reconciles it against reference data in Postgres, and generates a static HTML dashboard. The full task — rules, rubric, and the questions you must answer — is in the assignment brief sent to you by email.

## Quick start

```bash
git clone <this repo> lucy-tech-test
cd lucy-tech-test
docker compose up -d
python3.11 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

If the last command shows `1 passed` you're good to go.

## Architecture

```
 data/events.csv ─────┐
                      ├──► your pipeline ──► report.html
 Postgres (venues,    │
   daily_targets) ────┘
```

Postgres runs in Docker on `localhost:5432`. You ingest the CSV into storage of your choice (SQLite file, in-memory, or a new schema in the provided Postgres — your call). The pipeline exposes three CLI commands and writes a single self-contained `report.html` as its output.

## What's in the box

- `SOLUTION_TEMPLATE.md` — copy to `SOLUTION.md` and fill in as you go
- `data/events.csv` — the transactions you'll ingest
- `db/` — Postgres schema and seed data (auto-loaded on container start)
- `docker-compose.yml` — Postgres 16 service
- `src/cli.py` — stub entrypoint; you build out the three subcommands
- `tests/test_setup.py` — smoke test confirming Postgres and the CSV are reachable
- `pyproject.toml` — Python 3.11+, `psycopg2-binary`, `pytest`

## The task

See the assignment brief sent to you by email.

## Troubleshooting

- **Docker not running.** Start Docker Desktop (macOS/Windows) or `sudo systemctl start docker` (Linux), then `docker compose up -d`.
- **Port 5432 already in use.** If `docker compose up -d` fails with `port is already allocated` on 5432, you likely have another Postgres running. Either stop it (`brew services stop postgresql`, `sudo systemctl stop postgresql`, or `docker ps` + `docker stop …`), or remap: set `DATABASE_URL=postgresql://lucy:lucy@localhost:5433/lucy_test` in `.env` and change the `docker-compose.yml` port mapping to `"5433:5432"` (or export `POSTGRES_HOST_PORT=5433`).
- **Python version mismatch.** You need Python 3.11 or newer. `python3 --version` to check.
- **`psycopg2-binary` fails to install.** You're probably on an OS/arch without a prebuilt wheel — install Postgres client headers (`brew install libpq` / `apt install libpq-dev`) and retry.

## Contact

Email bjorn.treje@lucyanalytics.com if the starter doesn't run within 10 minutes of following Quick Start, or if anything in the assignment brief is unclear. If the starter is broken on your machine that's on us, not you.
