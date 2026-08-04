import os


def load_config():

    return {
        "days_ahead": int(
            os.getenv("DAYS_AHEAD", 3)
        ),

        "start_hour": int(
            os.getenv("START_HOUR", 15)
        ),

        "end_hour": int(
            os.getenv("END_HOUR", 22)
        ),

        "min_players": int(
            os.getenv("MIN_PLAYERS", 0)
        ),

        "timezone": os.getenv(
            "TIMEZONE",
            "Europe/Rome"
        )
    }
