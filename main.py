import json

from modules.limitless import get_vgc_tournaments
from modules.filters import filter_tournaments


def load_config():

    with open(
        "config.json",
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)



def main():

    config = load_config()

    print("Downloading tournaments...")

    tournaments = get_vgc_tournaments()

    print(
        f"Found {len(tournaments)} tournaments"
    )


    filtered = filter_tournaments(
        tournaments,
        config
    )


    print(
        f"After filters: {len(filtered)}"
    )


    for tournament in filtered:

        print("----------------")
        print(
            tournament.get("name")
        )
        print(
            tournament.get("start_date")
        )
        print(
            tournament.get("players")
        )



if __name__ == "__main__":
    main()
