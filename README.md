
# Bouncing DVD Logo with Pygame

This Python script creates a bouncing DVD logo simulation using the Pygame library. It features a DVD logo that moves around the screen, changes color, and plays a sound when it hits the edges of the window. The script also includes a full-screen mode toggle for an immersive experience.

## Features

- **Bouncing DVD Logo**: The logo moves around the screen, bouncing off the edges.
- **Color Tinting**: The logo's color changes dynamically over time.
- **Sound Effect**: A sound plays whenever the logo hits the edges of the screen.
- **Fullscreen Mode**: Press `F11` to toggle between fullscreen and windowed mode.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/) library

To install Pygame, run:
```bash
pip install pygame
```

## Usage

1. Clone this repository or download the script.
2. Ensure you have the following files located in the same directory as the script:
   - A logo image `DVD.png`
   - A sound file `Fart.mp3`
4. Run the script using:
   ```bash
   python DVD.py
   ```

## Controls

- `F11`: Toggle between fullscreen and windowed mode.
- `ESC`: Close the program.

## How It Works

- The logo starts at a random position and moves in a random direction.
- When it hits the edges of the screen, it bounces back in the opposite direction and plays a sound.
- The logo gradually changes its color for a dynamic visual effect.
- The user can switch to fullscreen mode for a better viewing experience.

## Customization

- **Change Image**: Replace the image at the specified path with another image of your choice.
- **Change Sound**: Replace `Fart.mp3` with another sound file to customize the sound effect.
- **Adjust Speed**: Modify the `dx` and `dy` variables in the script to change the speed of the logo.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Built using [Pygame](https://www.pygame.org/).
