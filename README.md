# Protein-Drug Affinity Prediction Scaffold

This repository contains a **minimal, placeholder-safe research scaffold** for protein-drug affinity prediction experiments.

## Project structure

- `configs/base.yaml` - baseline configuration placeholder
- `scripts/train.py` - placeholder training entrypoint
- `scripts/eval.py` - placeholder evaluation entrypoint
- `reports/` - save experiment summaries here
- `drafts/` - save draft text/notes here

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Placeholder-safe commands

These commands validate wiring and configuration loading only.
They do **not** train a real model or produce benchmark results.

```bash
python scripts/train.py --config configs/base.yaml
python scripts/eval.py --config configs/base.yaml
```

## Notes

- Do not report invented metrics or fabricated outcomes.
- Replace placeholder dataset/model paths in `configs/base.yaml` when implementing the real pipeline.
