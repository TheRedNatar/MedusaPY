
def prepare_row(row):

    ret = {
        # "inactive_in_current": row["inactive_in_current"],
        "n_days": row["n_days"],
        "distance_to_origin": row["distance_to_origin"],
        "prev_distance_to_origin": row["prev_distance_to_origin"],
        "center_mass_x": row["center_mass_x"],
        "center_mass_y": row["center_mass_y"],
        "n_villages": row["n_villages"],
        "n_village_decrease": row["n_village_decrease"],
        "n_village_increase": row["n_village_increase"],
        "total_population": row["total_population"],
        "total_population_decrease": row["total_population_decrease"],
        "total_population_increase": row["total_population_increase"],
        "player_id": row["player_id"]}

    return ret
