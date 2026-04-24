"""Placeholder evaluation entrypoint for protein-drug affinity prediction."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Placeholder evaluation script")
    parser.add_argument("--config", type=Path, required=True, help="Path to YAML config")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = args.config

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    print("[eval] Placeholder run only. No real evaluation is performed.")
    print(f"[eval] Loaded config from: {config_path}")
    print(f"[eval] Split: {config.get('data', {}).get('split', 'unknown')}")


if __name__ == "__main__":
    main()
