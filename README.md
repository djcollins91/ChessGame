# Chess Game (PyQt5)

This is a full-featured chess game implemented in Python using PyQt5 for the graphical user interface. The game supports all standard chess rules, including:

- Piece movement and capturing
- Turn-based play (White and Black)
- Check and checkmate detection
- Enforcement of legal moves (cannot put or leave your own king in check)
- Game ends automatically on checkmate

## Features
- **Modern GUI:** The chessboard and pieces are rendered with PyQt5, using custom piece images.
- **Robust Game Logic:** All chess rules are enforced, including check, checkmate, and illegal move prevention.
- **User Feedback:** The game provides clear messages for invalid moves, check, and checkmate situations.

## How to Run
1. Install dependencies:
   ```bash
   pip install PyQt5
   ```
2. Run the game:
   ```bash
   python main.py
   ```

## Project Structure
- `main.py` — Entry point for the application
- `game_board.py` — Main GUI and game logic
- `board.py`, `piece.py`, `place_pieces.py` — Board and piece setup
- `pieces/` — Piece logic (move, take_piece, etc.)
- `piece_images/` — Images for all chess pieces
- `tests/` — Unit tests for all piece logic

## How Generative AI Helped
This project was developed and debugged with the assistance of generative AI (GitHub Copilot). AI was used to:
- Refactor and optimize check and checkmate detection logic
- Debug and fix IndexError and logic bugs in piece movement and capturing
- Implement robust enforcement of chess rules (e.g., preventing moves that leave the king in check)
- Design and improve the PyQt5 GUI, including user feedback and board updates
- Suggest best practices for code structure and efficiency
- **Practice Test-Driven Development (TDD):** AI helped generate and refine unit tests for all chess piece logic, ensuring correctness and reliability through automated testing in the `tests/` directory

Generative AI accelerated the development process, provided solutions to complex chess logic, and ensured the GUI and game logic were robust, user-friendly, and well-tested through TDD.


