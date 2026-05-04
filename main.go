package main

import (
    "image/color"
    "log"
    "math"
    "github.com/hajimehoshi/ebiten/v2"
    "github.com/hajimehoshi/ebiten/v2/ebitenutil"
    "github.com/hajimehoshi/ebiten/v2/vector"
)

// 1. The Memory Footprint
type Particle struct {
    X, Y       float64
    VelX, VelY float64
    Mass       float64
}

// 2. The Engine State
type Game struct {
    Sun        Particle
    Planet     Particle
}

// 3. The Logic Loop (Runs 60 FPS)
func (g *Game) Update() error {
    // TODO: Gravity math goes here.
    dx := g.Sun.X - g.Planet.X
    dy := g.Sun.Y - g.Planet.Y
    distance := math.Sqrt(dx*dx + dy*dy)
    G := 0.15
    force := (G * g.Sun.Mass * g.Planet.Mass) / (distance * distance)
    // Note: Atan2 takes Y first, then X. This is a classic programming trap!
    angle := math.Atan2(dy, dx)
    forceX := force * math.Cos(angle)
    forceY := force * math.Sin(angle)
    g.Planet.VelX += forceX / g.Planet.Mass
    g.Planet.VelY += forceY / g.Planet.Mass
    g.Planet.X += g.Planet.VelX
    g.Planet.Y += g.Planet.VelY
    return nil
}

// 4. The Render Loop (Draws to screen)
func (g *Game) Draw(screen *ebiten.Image) {
    // Prints a debug message to the top left
    ebitenutil.DebugPrint(screen, "Gravity Engine Online. Particle initialized...")
    
    // TODO: Draw the actual particle to the screen here.
    vector.DrawFilledCircle(screen, float32(g.Sun.X), float32(g.Sun.Y), 10, color.White, true)
    vector.DrawFilledCircle(screen, float32(g.Planet.X), float32(g.Planet.Y), 10, color.RGBA{0, 0, 255, 255}, true)
}

// 5. The Screen Dimensions
func (g *Game) Layout(outsideWidth, outsideHeight int) (screenWidth, screenHeight int) {
    return 640, 480
}

// 6. The Boot Sequence
func main() {
    ebiten.SetWindowSize(640, 480)
    ebiten.SetWindowTitle("AppSec Gravity Engine")
    
    // Initialize the engine with our particle's starting position
    game := &Game{
        Sun: Particle{
            X:    320, // Center of the screen
            Y:    240,  // Center of the Screen
            VelX: 0,
            VelY: 0,
            Mass: 10000,
        },
        Planet: Particle{
            X: 100,
            Y: 240,
            VelX: 0,
            VelY: 1.8,
            Mass: 10,
        },
    }

    // Fire it up
    if err := ebiten.RunGame(game); err != nil {
        log.Fatal(err)
    }
}
