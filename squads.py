import pandas as pd

from setup import *


def create_squad_df() -> pd.DataFrame:
    """
    This extracts squad info for the FIFA World Cup 2022. May need to be adapted as the page gets updated.
    Saves a squads.csv file with columns "Position", "Player", "Team".

    :return: Pandas DataFrame of squad list.
    """
    create_folder()

    # List of teams in order of wikipedia page, by group then alphabetical.
    teams = ["Ecuador", "Netherlands", "Qatar", "Senegal",
             "England", "Iran", "United States", "Wales",
             "Argentina", "Mexico", "Poland", "Saudi Arabia",
             "Australia", "Denmark", "France", "Tunisia",
             "Costa Rica", "Germany", "Japan", "Spain",
             "Belgium", "Canada", "Croatia", "Morocco",
             "Brazil", "Cameroon", "Serbia", "Switzerland",
             "Ghana", "Portugal", "South Korea", "Uruguay"]

    # Import the tables from the wikipedia page of squads.
    squads = pd.read_html("https://en.wikipedia.org/wiki/2022_FIFA_World_Cup_squads")[:32]

    # Assign new column for the country.
    for team, squad in enumerate(squads):
        squad["Team"] = teams[team]

    # Remove columns not needed and clean data.
    squads_df = pd.concat(squads)
    squads_df = squads_df.dropna(axis=0, subset=["Player"])
    squads_df = squads_df.drop("No.", axis=1)
    squads_df = squads_df.rename(columns={"Pos.": "Position"})
    squads_df = squads_df.drop("Date of birth (age)", axis=1)
    squads_df = squads_df.drop("Caps", axis=1)
    squads_df = squads_df.drop("Goals", axis=1)
    squads_df = squads_df.drop("Club", axis=1)
    squads_df["Player"] = squads_df["Player"].str.replace(r" \(.*\)", "", regex=True)
    squads_df = squads_df.reset_index()
    squads_df = squads_df.drop("index", axis=1)

    # Save squad list to csv file.
    squads_df.to_csv(f"{TOURNAMENT}/squads.csv", index=False, encoding="utf-8-sig")

    return squads_df


if __name__ == "__main__":
    create_squad_df()
