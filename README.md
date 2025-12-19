# Alien Invasion

**Version: 1.0.0**

A classic space shooter game built with Python and Pygame, inspired by the iconic Space Invaders arcade game.

## About The Project

This is a complete game project I built to develop my Python programming skills and understand game development fundamentals. Players control a spaceship defending against waves of descending aliens, with increasing difficulty across multiple levels.

## Gameplay Demo
![Gameplay Demo](alien_invasion\game_play_demos\game_demo.gif)
*16 seconds of gameplay showing ship movement, alien destruction, and scoring*

## Features

- **Player Ship Controls**: Move up, down, left, and right using arrow keys
- **Shooting Mechanics**: Fire bullets with the spacebar (limited to 3 bullets on screen at once)
- **Alien Fleet**: Dynamically generated rows of aliens that move across and down the screen
- **Edge Detection**: Aliens change direction and drop down when reaching screen edges
- **Collision System**: Bullet management with automatic cleanup when bullets leave the screen
- **Start Button**: Launch the game using either the Play button or the P key for quick access

### Game Systems
- **Collision Detection**: Fully implemented bullet-to-alien and alien-to-ship collision systems
- **Scoring System**: Earn points for destroying aliens, with scores increasing at higher levels
- **High Score Tracking**: Your best score persists across game sessions
- **Lives System**: Start with 3 ships; lose a life when hit by aliens or when aliens reach the bottom
- **Progressive Difficulty**: Game speed and alien point values increase with each level
- **Level Progression**: Clear all aliens to advance to the next, more challenging level

### User Interface
- **Start Menu**: Launch the game using either the on-screen Play button or press P
- **Live Scoreboard**: Real-time display of current score, high score, current level, and remaining ships
- **Game Over State**: Returns to menu when all ships are lost, allowing restart

### Audio
- **Dynamic Background Music**: 
  - Menu music plays during game start screen and game over
  - Gameplay music activates during active play sessions
  - Music transitions seamlessly between game states
- **Sound Effects**: 
  - Shooting sound when bullets are fired
  - Explosion sound when aliens are destroyed
  - Audio feedback for enhanced game experience

## Tech Stack

- **Python 3**
- **Pygame** - Game development library

## Game Controls

| Key | Action |
|-----|--------|
| ↑ | Move ship up |
| ↓ | Move ship down |
| ← | Move ship left |
| → | Move ship right |
| SPACE | Fire bullet |
| P | Start game/Restart game |
| Q | Quit game |

## Project Structure

```
alien-invasion/
├── alien_invasion.py    # Main game loop and initialization
├── game_functions.py    # Game logic and helper functions
├── settings.py          # Game configuration and dynamic difficulty settings
├── ship.py             # Player ship class with movement logic
├── bullet.py           # Bullet class with firing mechanics
├── alien.py            # Alien class with fleet behavior
├── game_stats.py       # Game statistics tracking (score, lives, level)
├── score_board.py      # Scoreboard display and rendering
└── button.py           # UI button class for menu system
```
## How to Run

1. Make sure you have Python installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Navigate to the project root directory
4. Run the game:
   ```bash
   python alien_invasion.py
   ```

## Troubleshooting

**FileNotFoundError for images or sounds**
- Ensure you're running from the project root (not from inside subdirectories)
- Verify `images/` and `sounds/` folders exist with all assets


## Gameplay Mechanics

### Scoring
- Each alien destroyed earns points
- Point values increase with each level
- High score automatically saves and persists between sessions

### Difficulty Progression
- Ship speed increases each level
- Alien speed increases each level
- Bullet speed increases each level
- Alien point values scale up with difficulty

### Win/Loss Conditions
- **Win a level**: Destroy all aliens before they reach the bottom or hit your ship
- **Lose a life**: Get hit by an alien or allow aliens to reach the screen bottom
- **Game Over**: All three ships destroyed


## What I Learned

- **Object-Oriented Programming**: Organized code using classes for different game entities
- **Game Loop Fundamentals**: Implemented continuous game state updates and rendering
- **Event Handling**: Managed keyboard inputs and game events
- **Sprite Groups**: Used Pygame's Group class for efficient sprite management
- **Collision Detection**: Implemented basic collision systems
- **Code Organization**: Separated concerns across multiple modules for maintainability
- **Audio Integration**: Implemented dynamic background music system that responds to game states, with separate tracks for menu and gameplay
- **Game Polish**: Added audio feedback and music transitions to improve game feel and user engagement

## Current Status

**Project Status: Complete** ✅

This project is fully functional with all planned core features implemented. The game is playable, stable, and demonstrates solid understanding of game development principles.

### Completed Features
✅ Ship movement in all four directions  
✅ Bullet firing system with ammunition limit  
✅ Dynamic alien fleet generation  
✅ Alien movement patterns with edge detection  
✅ Complete collision detection system  
✅ Scoring and high score tracking  
✅ Lives/health system  
✅ Game over and restart functionality  
✅ Progressive difficulty scaling  
✅ Level progression system  
✅ Interactive start menu  
✅ Live scoreboard display  
✅ Sound effects and background music


### Future Enhancements
- Custom start menu with settings options
- Power-ups and special weapons


## Code Highlights

This project demonstrates:
- Clean separation of concerns across multiple modules
- Efficient use of Pygame's sprite and group systems
- Dynamic difficulty scaling based on game progression
- Proper game state management
- Professional code organization and documentation

## Acknowledgments

This project was built by following Eric Matthes' *Python Crash Course* tutorial, with my own extensions, modifications, and original audio content.

**Audio:** Background music and sound effects created by me.

---

*This is a personal learning project that demonstrates practical application of programming concepts in game development.*