from datetime import datetime

import pytz

from modules.config import load_config
from modules.limitless import get_vgc_tournaments
from modules.filters import filter_tournaments
from modules.discord_sender import send_discord_message
from modules.storage import (
    is_posted,
    mark_as_posted
)


def prepare_tournaments(tournaments, config):

    timezone = pytz.timezone(
        config["timezone"]
    )

    result = []

    for t in tournaments:

        # Salta quelli già inviati
        if is_posted(t["id"]):
            continue


        # Conversione da UTC a ora italiana
        date = datetime.fromisoformat(
            t["date"]
        )

        local_date = date.astimezone(
            timezone
        )


        # Timestamp Unix per Discord
        t["discord_timestamp"] = int(
            local_date.timestamp()
        )


        result.append(t)


    return result



def main():

    config = load_config()


    print(
        "Downloading tournaments..."
    )


    tournaments = get_vgc_tournaments()


    print(
        f"Found {len(tournaments)} upcoming tournaments"
    )


    filtered = filter_tournaments(
        tournaments,
        config
    )


    print(
        f"After filters: {len(filtered)}"
    )


    new_tournaments = prepare_tournaments(
        filtered,
        config
    )


    print(
        f"New tournaments: {len(new_tournaments)}"
    )


    if not new_tournaments:
        return


    # Invia su Discord
    if send_discord_message(
        new_tournaments
    ):

        # Salva solo se Discord ha risposto correttamente
        for tournament in new_tournaments:

            mark_as_posted(
                tournament["id"]
            )


if __name__ == "__main__":
    main()
