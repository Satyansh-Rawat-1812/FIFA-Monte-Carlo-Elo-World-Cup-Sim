import pandas as pd

elo_df = pd.read_csv("../data/team_elo_ratings.csv")

elo_dict = dict(
    zip(
        elo_df["team"],
        elo_df["elo"]
    )
)

elo_dict["Argentina"]
