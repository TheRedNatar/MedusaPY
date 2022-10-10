from collections import Counter
import random

def split_x_y_pid(df):
    y = df.y.values
    p_id = df.player_id.values
    X = df.drop(columns=["y", "player_id"]).values
    return (X, y, p_id)


def select_players(data, sample_in_test):
    ids = [x["player_id"] for x in data]
    p_id_freq = dict(Counter(ids))
    l_s = list(p_id_freq.items())

    random.shuffle(l_s)

    total_s = len(data)
    acc = 0
    i = 0
    sample_in_test = 0.33
    perc = sample_in_test * total_s
    included = []
    while acc < perc: 
        item = l_s[i]
        acc += item[1]
        included.append(item[0])
        i += 1
    
    return included