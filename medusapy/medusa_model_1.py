
def prepare_row(row):

    ret = {
        "distance_to_origin": row["distance_to_origin"],
        "center_mass_x": row["center_mass_x"],
        "center_mass_y": row["center_mass_y"],
        "n_villages": row["n_villages"],
        "total_population": row["total_population"],
        "player_id": row["player_id"]}

    return ret
