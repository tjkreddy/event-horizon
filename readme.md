# Event Horizon

A high-performance 2D Newtonian physics engine and N-body orbital mechanics simulator written in Go. 

This project is built to explore low-level memory management, struct architecture, and rendering loops in a statically typed, compiled language. It serves as a foundational exercise in systems engineering and mathematical rendering.

## 🎯 Motivation: Systems Engineering & AppSec

In the realm of Application Security and Systems Architecture, understanding how memory is allocated, how pointers are passed, and how CPU cycles are consumed is the difference between a scripter and an engineer.

This project was built to intentionally step away from high-level scripting and dive into the mechanics of a compiled language. Building an N-Body physics engine requires strict state management, memory-efficient data structures (Go Slices and Pointers), and a deep understanding of computational complexity ($O(N^2)$ time complexity for gravitational calculations).

By simulating physical laws at 60 frames per second, I am building the exact same foundational skills—memory safety, execution speed, and algorithmic efficiency—required to develop high-performance security infrastructure, custom malware analysis frameworks, and lightning-fast network tools.

## 🚀 Architecture & Tech Stack

* **Language:** Go (Golang)
* **Graphics Engine:** [Ebitengine](https://ebiten.org/) (v2)
* **Physics:** Custom Newtonian kinematics and trigonometric force vectors

## ⚙️ Core Features

* **Newtonian Gravitation:** Calculates dynamic gravitational pull between masses using $F = G \frac{m_1 m_2}{r^2}$.
* **Trigonometric Force Vectors:** Utilizes `math.Atan2` for accurate trajectory plotting and vector splitting across the X and Y axes.
* **Singularity Clamping:** Implements mathematical distance floors to prevent division-by-zero errors and infinite velocity slingshots during close-proximity orbital passes.
* **Strict Type Casting:** Securely manages memory by handling high-precision `float64` physics math and safely casting to `float32` for GPU rendering.

## 🛠️ Installation & Execution

Ensure you have [Go](https://go.dev/) installed on your system.

```bash
# Clone the repository
git clone [https://github.com/tjkreddy/event-horizon.git](https://github.com/tjkreddy/event-horizon.git)

# Navigate into the directory
cd event-horizon

# Pull engine dependencies
go mod tidy

# Compile and run the engine
go run main.go
