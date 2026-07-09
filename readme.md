# Gravity Sim

A 2D Newtonian gravity simulator written in Python with Pygame. Built as a weekend side quest to learn programming, physics, and orbital mechanics.

## Tech Stack

- **Language:** Python 3
- **Graphics:** Pygame
- **Physics:** Custom Newtonian gravity (`F = G * m1 * m2 / r²`)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install pygame
python main.py
```

## Features

- Newtonian gravity (`F = G * m1 * m2 / r²`) with Euler integration
- Orbital simulation with configurable particle masses and velocities
- Implemented as a `Particle` class with encapsulated `update()` and `draw()` methods
- Frame-capped at 60 FPS for consistent simulation speed

## Controls

Close the window to exit.
