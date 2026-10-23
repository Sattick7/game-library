# Game Library

A command-line app to track the games you own, play, and want to play.
Built in Python as a learning project. The project can be used to track their games, without linking their accounts or anything, it's just a tracker.


## Features

- Add games with a title, platform, and status
- List all games
- Search by part of a title (not case-sensitive)
- Update a game's status
- Remove a game
- Saves automatically to `games.json` and loads it on startup
- Input checks: no blank fields, no duplicate titles, valid statuses only

Valid statuses: `playing`, `finished`, `wishlist`, `abandoned`

## Requirements

- Python 3.10 or newer
- pytest (only to run the tests)

## How to run

1. Clone the repo: `git clone https://github.com/Sattick7/game-library.git`
2. Go into the folder: `cd game-library`
3. Run: `python main.py`
4. Pick an option from the menu.

## How to run the tests

    python -m pip install pytest
    python -m pytest

All 20 tests should pass.

## Limitations

- Titles must be typed exactly (ignoring capitals) to remove or update a game.
- Only the status can be updated, not the title or platform.
- Duplicates are detected by title only, so the same game on two platforms is refused.
- Data lives in `games.json` next to the program, so running it from another folder starts a new library.
- If `games.json` is damaged, the program starts empty and the next save overwrites the broken file.
- No sorting or filtering by platform or status.

## What I learned

I learned a lot during this project... It was a good text for DSA, as well as other elements such as pytest. I also learned how to use json file to save the data. Mainly to use git in my project.

## Future ideas

- Basic graphical interface (tkinter)
- Edit title and platform, not just status
- Filter by platform or status
- To add a database of game title so people can just choose from a dropdown list