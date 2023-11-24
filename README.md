# Simple Python MemoryGame!

## Description

MemoryGame is a simple command-line game where you have to decide if you've seen a word before or if it's new to you.
The goal is to achieve the highest score by making the right choices.

## Features

- Randomly selects words from a word list.
- Tracks and saves a record of the highest score.
- Provides an interactive and engaging gameplay experience.

## Requirements

- Python 3.x

## How to Play

1. Run the game by executing the `launch_game.py` script.
2. You will be presented with a word, and you need to choose if you have seen it before or if it's new.
3. Enter '1' for SEEN or '2' for NEW.

## Installation

1. Clone the repository: `git clone https://github.com/VictorMusta/MemoryGame.git`
2. Navigate to the project folder: `cd MemoryGame`
3. Run the game: `python3 -m launch_game.py`

## Files

- `launch_game.py`: The main script for the game.
- `ressources/word_list.txt`: Contains the list of words for the game.
- `ressources/seen_words_list.txt`: Keeps track of words that have been seen.
- `ressources/record.txt`: Stores the highest score.
- `old_launch_game.py`: The deprecated main script for the game. (the new one have been optimized with chatGPT, this one
  is made by hand without any AI help.)

## Author

Victor Grabowski
