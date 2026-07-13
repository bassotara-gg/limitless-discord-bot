import json
import os


def load_config():

    with open("config.json", encoding="utf-8") as f:
        config = json.load(f)

    config["days_ahead"] = int(
        os.getenv("DAYS_AHEAD", config["days_ahead"])
    )

    config["start_hour"] = int(
        os.getenv("START_HOUR", config["start_hour"])
    )

    config["end_hour"] = int(
        os.getenv("END_HOUR", config["end_hour"])
    )

    config["min_players"] = int(
        os.getenv("MIN_PLAYERS", config["min_players"])
    )

    return config
