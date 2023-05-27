
def prepare_row(row):

    new_row = row.copy()

    del new_row["target_dt"]
    del new_row["server_id"]

    return new_row
