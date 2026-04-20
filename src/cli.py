"""Candidate entrypoint for the Lucy tech-test pipeline.

Three subcommands:

    python -m src.cli import-csv        # full ingest, must be idempotent
    python -m src.cli rerun             # re-process one (venue, business_date)
    python -m src.cli generate-report   # write report.html

Each subcommand is a stub — you implement the behaviour. See the
assignment brief (sent by email) for required behaviour and the four
dashboard sections ``report.html`` must contain.
"""

from __future__ import annotations

import argparse
import sys


def _cmd_import_csv(args: argparse.Namespace) -> int:
    print(f"import-csv: not implemented — this is where you build "
          f"(csv_path={args.csv_path})")
    return 0


def _cmd_rerun(args: argparse.Namespace) -> int:
    print(f"rerun: not implemented — this is where you build "
          f"(business_date={args.business_date}, venue={args.venue})")
    return 0


def _cmd_generate_report(args: argparse.Namespace) -> int:
    print(f"generate-report: not implemented — this is where you build "
          f"(output={args.output})")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.cli",
        description="Lucy tech-test pipeline CLI.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_import = sub.add_parser(
        "import-csv",
        help="Full ingest of the events CSV. Must be idempotent.",
    )
    p_import.add_argument(
        "--csv-path",
        default="data/events.csv",
        help="Path to the events CSV (default: data/events.csv).",
    )
    p_import.set_defaults(func=_cmd_import_csv)

    p_rerun = sub.add_parser(
        "rerun",
        help="Re-process one (venue, business_date) batch. Must be idempotent.",
    )
    p_rerun.add_argument("--business-date", required=True, help="YYYY-MM-DD")
    p_rerun.add_argument("--venue", required=True, help="venue_id, e.g. v_sto")
    p_rerun.set_defaults(func=_cmd_rerun)

    p_report = sub.add_parser(
        "generate-report",
        help="Write the static HTML dashboard.",
    )
    p_report.add_argument(
        "--output",
        default="report.html",
        help="Output HTML path (default: report.html).",
    )
    p_report.set_defaults(func=_cmd_generate_report)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
