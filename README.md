# OOPMineseeper
A terminal-based Minesweeper game using OOP written in python

### Tabel of contents
- Description of the project
- Reqirements
- Installation
- UML
- Example run
- Code conventions
- Contrbution
- Changelog
- Contact
- License

### Description of the project
A terminal-based Minesweeper game with ascii graphics.  Players will be able to play on their own device and compare their highscores to friends.  You play by inputing coordinates for the square you want to explore, it'll be possible to flag it or clear it.  If the square is safe, a number (of the amount of surrounding bombs) will replace it.  Score is based on the ammount of cleared squares and with a multiplier that decreases with the ammount of flags placed and the time it takes to complete it, fewer flags means higher score.  It will be possible to compare score with other players within the program, in between games.

### Requriemnts
- Python 3.6+
- `random` module

### Installation
`WIP`

### Code conventions
**File organisation:**  the code is divided into different files containing classes, textfiles and the `main` file

### UML
![image](https://user-images.githubusercontent.com/96416409/171232397-0db0db47-4800-4d45-aaf4-a8b73fa2246a.png)


### Example run
There is no working version as of yet

### Contribution
Pull requests will not be accepted because this is a school project

### Changelog
**v0.1**

The basic bunctions of the game are done

**v0.5**

Added:
- Score based on number of bombs, time and squares cleared
- Save/Load game will resume previous gamestate
- Clears multiple lines when empty square is revealed
- Tutorial for how to play
- Customizable attributes: board size & difficulty

Fixed:
- More fool-proof imput

**v1.0**

Added:
- Able to post score to a server
- Online leaderboard

### Contact
**Author:**  Bernard R [Bern4rdR]

**Mail:**  [rumarbernard@gmail.com](mailto:rumarbernard@gmail.com)

**Discord:**  BernHard#6216

### Licence
[MIT](https://choosealicense.com/licenses/mit/)
