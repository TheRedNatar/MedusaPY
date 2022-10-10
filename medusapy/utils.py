

def create_tribes_dict(tribes_dict):
    default = {
        "romans": 0,
        "teutons": 0,
        "gauls": 0,
        "nature": 0,
        "natars": 0,
        "huns": 0,
        "egyptians": 0,
        "spartans": 0
    }
    default.update(tribes_dict)

    return default
