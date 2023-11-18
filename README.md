# Underrail-Mutagen-Solver

Brute force solver for the Mutagens puzzle for the game Underrail. This solver is not in any way optimal as given the combinatorial nature of the puzzle, the solver has to iterate on 15! (~= 1.3*10^12) possible combinaison. Some very basic prunning rules are used to reduce this amount.

## Usage

- mutagens.txt should contain the sequence for each mutagen
- exitus.txt should contain the sequence of the target Exitus mutagen
- Respect the same syntax
- While in-game, CTRL+C allows you to copy the current dialogue to paste the mutagen sequence
- 
        python3 solver.py

## Rules of the mutagens puzzle
The rules of the puzzle are avaible on the [official wiki](https://www.stygiansoftware.com/wiki/index.php?title=Mutagen_Puzzle). Contains slight spoilers about the end game of Underrail. 