# Typing Game

A simple Python-based command-line typing game where you can practice your typing speed and accuracy. The game displays random prompts, and you need to type them as quickly and accurately as possible. If you type the prompt correctly, you'll receive a congratulations message. If there are errors, the mistyped characters are highlighted in red.

## Installation*

Before running the game, make sure to install the required module:

```bash
pip install colorama
```

## Features

- **Random Prompts:** The game provides a variety of prompts to keep your typing practice interesting.

- **Typing Speed Calculation:** After each round, your typing speed in words per minute is displayed.

- **Mistake Highlighting:** If you make an error while typing, the mistyped characters are highlighted in red, helping you identify and correct your mistakes.

- **Colorful Output:** The game uses the `colorama` library to make the output colorful. The congratulations message is displayed in green.

- **Customizable Prompts:** You can easily add more prompts to the game by extending the `prompts` list.

## Usage

1. Run the typing game script:

```bash
python typing.py
```

2. You'll be presented with a random prompt. Type the prompt as accurately and quickly as possible.

3. If you type the entire prompt correctly, you'll receive a congratulations message in green.

4. If there are errors, the mistyped characters will be highlighted in red.

5. After each round, the game will display your typing speed in words per minute.

6. You can choose to play the game again or exit.

## Additional Prompts

You can customize the list of prompts in the `prompts` list in the script. Simply add more sentences to expand the variety of typing exercises.
