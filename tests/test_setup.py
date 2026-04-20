"""Smoke test: Postgres reachable and events CSV readable.

Does not exercise any business logic — that's the candidate's job. This
test is only here to confirm the starter is wired up correctly on the
candidate's machine.
"""

from __future__ import annotations

import csv
import os
import sys
from pathlib import Path

import pytest

try:
    import psycopg2
except ImportError:  # pragma: no cover - psycopg2 is a declared dependency
    psycopg2 = None  # type: ignore[assignment]

REPO_ROOT = Path(__file__).resolve().parent.parent
EVENTS_CSV = REPO_ROOT / "data" / "events.csv"
DEFAULT_DB_URL = "postgresql://lucy:lucy@localhost:5432/lucy_test"


def _database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if url is None:
        print(
            "DATABASE_URL not set — defaulting to localhost:5432. "
            "Set it in .env if port 5432 conflicts on your machine.",
            file=sys.stderr,
        )
        return DEFAULT_DB_URL
    return url


def test_setup() -> None:
    # --- CSV side ---------------------------------------------------------
    assert EVENTS_CSV.exists(), (
        f"{EVENTS_CSV} is missing — did the starter include data/events.csv?"
    )
    with EVENTS_CSV.open(encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh)
        header = next(reader, None)
        assert header is not None, "events.csv has no header row"
        required = ["transaction_id", "venue_id", "local_timestamp",
                    "amount_eur", "payment_method"]
        assert header[:5] == required, f"unexpected header: {header}"
        row_count = sum(1 for _ in reader)
    assert 2300 <= row_count <= 2500, (
        f"events.csv has {row_count} rows; expected 2,300–2,500"
    )

    # --- Postgres side ----------------------------------------------------
    if psycopg2 is None:
        pytest.skip("psycopg2 not installed — run `pip install -e '.[dev]'`")

    try:
        conn = psycopg2.connect(_database_url(), connect_timeout=3)
    except psycopg2.OperationalError as exc:
        pytest.skip(
            "Postgres not reachable — run `docker compose up -d` "
            f"(DATABASE_URL={_database_url()!r}, error: {exc})"
        )
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM venues")
            (venue_count,) = cur.fetchone()
        assert venue_count == 5, (
            f"expected 5 venues in Postgres, got {venue_count}"
        )
    finally:
        conn.close()
