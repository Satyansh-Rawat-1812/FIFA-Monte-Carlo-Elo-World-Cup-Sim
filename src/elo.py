def expected_score(rating_a, rating_b):
    return 1 / (1 + 10 ** ((rating_b - rating_a) / 400))

def actual_scores(home_score, away_score):

    if home_score > away_score:
        return 1, 0

    elif home_score < away_score:
        return 0, 1

    else:
        return 0.5, 0.5