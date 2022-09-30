import pickle
import datetime


def prepare_row(row):
    date = datetime.date.fromisoformat(row["date"])
    weekday = date.weekday()
    return {
        "do": row["distance_to_origin"],
        "weekend": weekday in [5, 6],
        "weekday": weekday,
        "n_villages": row["n_villages"],
        "total_population": row["total_population"],
        "player_id": row["player_id"]
    }
