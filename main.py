import numpy as np
import pandas as pd

from setup import *


def pot_luck_players(squads: pd.DataFrame) -> None:
    """
    Takes in a Pandas DataFrame and uses a list of people in people.csv to randomly assign each player to a person.

    :param squads: Pandas DataFrame with list of players. Columns needed are "Position", "Player", "Team".
    """
    create_folder()

    # List of entrants.
    people = pd.read_csv(f"{TOURNAMENT}/people.csv", header=None)[0].values.tolist()

    # Randomise the squad list.
    squads_random = squads.sample(frac=1)

    # Set the number of players and people.
    num_players = len(squads_random)
    num_people = len(people)

    # Set the players per person and how many spare players.
    players_pp, spare = divmod(num_players, num_people)

    # Add column for person and assign by looping through people.
    squads_random["Person"] = np.tile(people, players_pp + 1)[:num_players]

    # Overwrite spare players so each person has the same number of players.
    if spare != 0:
        squads_random.loc[squads_random.index[-spare:], "Person"] = "Spare"

    # Add categorical order for Position column.
    squads_random["Position"] = pd.Categorical(squads_random["Position"], POSITIONS)

    # Get break down of how many players of each position people have.
    pos_distribution = squads_random.pivot_table(index="Person", columns="Position", aggfunc="size", fill_value=0)
    pos_distribution.to_csv(f"{TOURNAMENT}/person_position.csv", encoding="utf-8-sig")

    # Get break down of how many players of each team people have.
    pos_distribution = squads_random.pivot_table(index="Person", columns="Team", aggfunc="size", fill_value=0)
    pos_distribution.to_csv(f"{TOURNAMENT}/person_team.csv", encoding="utf-8-sig")

    # Sort to group by person.
    squads_random = squads_random.sort_values(by=["Person", "Team", "Position", "Player"])

    # Save assigned list of players to html and csv.
    squads_random.to_html(f"{TOURNAMENT}/pot_luck_players.html", index=False)
    squads_random.to_csv(f"{TOURNAMENT}/pot_luck_players.csv", index=False, encoding="utf-8-sig")


if __name__ == "__main__":
    squads_df = pd.read_csv(f"{TOURNAMENT}/squads.csv")
    pot_luck_players(squads=squads_df)
