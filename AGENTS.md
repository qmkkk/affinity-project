# AGENTS.md

## Goal
This repository is for protein-drug affinity prediction experiments.

## Rules
- Prefer minimal changes.
- Do not invent metrics or results.
- Save summaries to reports/.
- Save draft text to drafts/.
- Before finishing, run the smallest valid test.

## Commands
- Train: python scripts/train.py --config configs/base.yaml
- Eval: python scripts/eval.py --config configs/base.yaml
- Test: pytest -q
