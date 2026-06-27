# Contributing to Event Horizon

Thank you for your interest in contributing to Event Horizon! Whether you are optimizing the N-body physics math or tweaking the rendering loop, your help is appreciated.

## 🛠️ Local Development Setup

To set up the physics engine locally:

**1. Fork and clone the repository:**

```bash
git clone [https://github.com/YOUR_USERNAME/event-horizon.git](https://github.com/YOUR_USERNAME/event-horizon.git)
cd event-horizon
2. OS-Specific Dependencies (Ebitengine):
Because this engine uses Ebitengine for rendering, Linux users may need a few Cgo dependencies before it will compile.

Ubuntu/Debian: sudo apt install libc6-dev libgl1-mesa-dev libxcursor-dev libxi-dev libxinerama-dev libxrandr-dev libxxf86vm-dev libasound2-dev pkg-config

macOS/Windows generally compile out of the box.

3. Pull Go Modules:

Bash
go mod tidy
4. Run the Simulation:

Bash
go run main.go
🐛 Found a Bug?
Check existing Issues on GitHub to see if it has already been reported.

If not, open a new issue. Please include your OS, Go version, and a brief description of the visual or mathematical glitch.

✨ Adding a Feature
If you want to add a major feature (e.g., Barnes-Hut optimization, collision physics), please open an Issue first to discuss the architecture.

Keep the focus on zero-allocation rendering loops and memory safety.

🔀 Pull Request Process
Format your code using the standard Go formatter before committing:

Bash
go fmt ./...
Ensure your math operations safely cast between float64 (physics) and float32 (rendering).

Submit your PR against the main branch.

⚖️ License
By contributing, you agree that your contributions will be licensed under the project's GPLv3 License.
