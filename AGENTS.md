# Gravity Sim — Agent Guide

## Run

```bash
source venv/bin/activate && python main.py
```

Dependency: `pip install pygame` (only dep, no requirements.txt).

## Repo structure

Single-file app — everything is in `main.py`. No tests, no linter, no typechecker, no CI. Do not run any build/test/lint commands; they don't exist.

## Key code facts

- `Particle.update(self, other, G)` and `Particle.draw(self, screen, color, radius)` are **stub methods** — they have doc-comment placeholders but no implementation.
- The main loop does the gravity calculation inline (lines 31–44) instead of calling `update()`.
- Physics: simple Euler integration per frame (no delta-time). `F = G * m1 * m2 / r²`, velocity then position.
- The `Particle` class is the core abstraction; the sim currently has two instances (`sun`, `planet`).

## Workflow

This is a learning project. Features are added incrementally by choosing tasks from AGENTS.md or the conversation. Always read the current `main.py` before making changes — the code evolves each session.

## Constraints

- GPLv3 licensed (`LICENSE` file).
- `venv/` and `__pycache__/` are gitignored.
- macOS target, Python 3.
