"""Placeholder training entrypoint for protein-drug affinity prediction."""

from __future__ import annotations

import argparse
from pathlib import Path

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Placeholder training script")
    parser.add_argument("--config", type=Path, required=True, help="Path to YAML config")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config_path = args.config

    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    with config_path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    print("[train] Placeholder run only. No real model training is performed.")
    print(f"[train] Loaded config from: {config_path}")
    print(f"[train] Experiment name: {config.get('experiment', {}).get('name', 'unknown')}")


if __name__ == "__main__":
    main()
