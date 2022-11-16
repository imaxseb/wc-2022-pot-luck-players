from pathlib import Path

TOURNAMENT = "FIFA World Cup 2022"
POSITIONS = ["GK", "DF", "MF", "FW"]


def create_folder():
    """
    Creates folder with the tournament name if it doesn't already exist.
    """
    filepath = Path(TOURNAMENT)
    filepath.mkdir(exist_ok=True)


if __name__ == "__main__":
    create_folder()
