# main.py

This is the main entry point for the Chess application.

## Purpose
- Initializes the PyQt5 application and sets up the chess board with all pieces in their starting positions.
- Places all black and white pieces (pawns, rooks, knights, bishops, queens, kings) on the board using their respective classes and helper methods.
- Launches the graphical interface for the chess game using the `GameBoard` class.

## How it Works
1. Creates a `QApplication` instance for the GUI.
2. Instantiates a `Board` object.
3. Places all chess pieces in their correct starting positions using loops and helper methods from each piece class.
4. Creates a `GameBoard` object with the initialized board and displays it.
5. Starts the Qt event loop.

## Usage
Run this file to start the chess game:

```sh
python main.py
```

## Dependencies
- Python 3.10+
- PyQt5
- All chess piece modules and helpers in the `Pieces/` directory

## Notes
- Make sure all dependencies are installed and the directory structure is intact.
- This file should be run from the root of the project or with the correct Python path set.
