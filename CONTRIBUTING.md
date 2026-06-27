# Contributing to Event Horizon

Thank you for taking the time to contribute to **Event Horizon**! This project is a high-performance 2D Newtonian physics engine and N-body orbital mechanics simulator built to explore systems engineering, low-level memory management, and computational efficiency in Go.

By contributing, you help make this simulation faster, more mathematically precise, and a better learning resource for everyone.

---

## 🗺️ Code of Conduct
* Be respectful, collaborative, and constructive.
* Focus reviews on code efficiency, algorithmic correctness, and systemic optimization.

---

## 🛠️ Local Development Environment Setup

To hack on the physics engine locally, you need a functioning Go environment and the native graphic library dependencies for your operating system.

### 1. System Dependencies (Ebitengine v2)
Because this engine runs at 60 FPS using GPU rendering via Cgo, you must install the following development headers before compilation:

* **Ubuntu / Debian:**
  ```bash
  sudo apt update
  sudo apt install libc6-dev libgl1-mesa-dev libxcursor-dev libxi-dev libxinerama-dev libxrandr-dev libxxf86vm-dev libasound2-dev pkg-config

```

* **Fedora / RHEL:**
```bash
sudo dnf install mesa-libGL-devel libXcursor-devel libXrandr-devel libXinerama-devel libXi-devel libXxf86vm-devel alsa-lib-devel pkgconfig

```


* **macOS:** Requires Xcode Command Line Tools installed (`xcode-select --install`).
* **Windows:** Requires a valid GCC toolchain (e.g., via MSYS2 / MinGW-w64) added to your system `PATH`.

### 2. Fork and Clone

```bash
git clone [https://github.com/YOUR_USERNAME/event-horizon.git](https://github.com/YOUR_USERNAME/event-horizon.git)
cd event-horizon

```

### 3. Initialize & Run

```bash
# Verify modules and clean up dependencies
go mod tidy

# Run the simulation locally
go run main.go

```

---

## 🧠 Architectural & Optimization Guidelines

Event Horizon handles heavy mathematical computations ($O(N^2)$ algorithmic complexity for raw gravitational lookups) within a continuous rendering frame loop. To maintain a smooth 60 FPS target, please follow these core constraints:

* **Zero-Allocation Rendering Loops:** Avoid allocating memory inside the update or draw sequences. Re-use existing pointers and slices where possible. Avoid unnecessary object instantiations to prevent the Go Garbage Collector (GC) from causing frame stutters.
* **Precision Control:** All physical force vectors, trigonometric positions, and velocities must use high-precision `float64` primitives. Only cast down to `float32` explicitly during final coordinate mappings for GPU draw commands.
* **Vector Closures:** Use standard mathematical operations from the built-in `math` package (e.g., `math.Atan2`, `math.Sqrt`). Ensure your distance calculation logic implements the singularity clamp to prevent division-by-zero or infinite velocity vectors.

---

## 🐛 Submitting Issues & Feature Requests

### Reporting Bugs

1. Search the **Issues** tab to see if the bug has already been tracked.
2. If opening a new issue, explicitly state:
* Your Operating System and desktop environment (e.g., Linux Wayland vs X11).
* Your Go compiler version (`go version`).
* Step-by-step instructions to reproduce the anomaly or graphical stutter.



### Proposing Enhancements

If you wish to introduce a major system change (e.g., implementing a quad-tree / Barnes-Hut algorithm for $O(N \log N)$ optimization, adding inelastic collisions, or implementing elastic grid vectors):

* Open an **Issue** tagged with `enhancement` first to discuss the programmatic layout and execution path before writing code.

---

## 🔀 Workflow & Pull Request Process

We maintain clean, readable Git history histories. Follow these steps when sending code back upstream:

1. **Branch Naming:** Create a topical branch off of your local up-to-date fork:
```bash
git checkout -b feature/your-optimization-name
# OR
git checkout -b fix/issue-description

```


2. **Code Formatting:** Run the standard compiler formatting tools. Your PR will be rejected if it fails linting checks:
```bash
go fmt ./...
go vet ./...

```


3. **Commit Messages:** Use clear, declarative structural commit messages (e.g., `feat: optimize vector loop allocations` or `fix: add singularity clamp on close passes`).
4. **Submit PR:** Issue the pull request directly into our repository's `main` or `master` branch.

---

## ⚖️ License

By contributing to Event Horizon, you explicitly agree that your structural additions, patches, and code changes will be bound by the project's **GNU General Public License v3.0 (GPLv3)**.

```

### Step 3: Save and Push to GitHub

Once saved, stage it, commit it, and update your repository:

```bash
git add CONTRIBUTING.md
git commit -m "docs: implement professional Go-focused CONTRIBUTING guide"
git push

```
