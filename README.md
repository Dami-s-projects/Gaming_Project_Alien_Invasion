# Alien Invasion

A classic space shooter game built with Python and Pygame, inspired by the iconic Space Invaders arcade game.

## About The Project

This is a learning project I built to develop my Python programming skills and understand game development fundamentals. The player controls a spaceship that can move in all directions and shoot bullets at descending waves of aliens.

## Features

- **Player Ship Controls**: Move up, down, left, and right using arrow keys
- **Shooting Mechanics**: Fire bullets with the spacebar (limited to 3 bullets on screen at once)
- **Alien Fleet**: Dynamically generated rows of aliens that move across and down the screen
- **Edge Detection**: Aliens change direction and drop down when reaching screen edges
- **Collision System**: Bullet management with automatic cleanup when bullets leave the screen
- **Start Button**: Launch the game using either the Play button or the P key for quick access

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
| P | Start game |
| Q | Quit game |

## Project Structure

```
alien-invasion/
├── alien_invasion.py    # Main game loop
├── game_functions.py    # Game logic and helper functions
├── settings.py          # Game configuration settings
├── ship.py             # Player ship class
├── bullet.py           # Bullet class
├── game_stats.py       #Class tracks statistics like score and High scores
├── button.py           #Class creates button that is displayed on screen
├── score_board.py #class displays tracked statistics of game_stats on screen.
└── alien.py            # Alien class
```

## How to Run

1. Make sure you have Python installed
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Run the game:
   ```bash
   python alien_invasion.py
   ```

## What I Learned

- **Object-Oriented Programming**: Organized code using classes for different game entities
- **Game Loop Fundamentals**: Implemented continuous game state updates and rendering
- **Event Handling**: Managed keyboard inputs and game events
- **Sprite Groups**: Used Pygame's Group class for efficient sprite management
- **Collision Detection**: Implemented basic collision systems
- **Code Organization**: Separated concerns across multiple modules for maintainability

## Current Status

This project is currently completed. The project, however, is open to contributions.

### Working Features
✅ Ship movement in all directions  
✅ Bullet firing with limit system  
✅ Alien fleet generation  
✅ Aliens moving and changing direction at edges  
✅Collision detection between bullets and aliens
✅Implement scoring system
✅Game over and restart functionality
✅Implemented increasing difficulty levels

### Planned Improvements
- Create start menu
- Add sound effects

## Acknowledgments

This project was built while following along with learning resources and adapted with my own modifications to reinforce my understanding of Python and game development concepts.

---

*This is a personal learning project created as part of my journey in software development.*