import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone


BASE_URL = "https://play.limitlesstcg.com"


def get_vgc_tournaments():

    response = requests.get(
        f"{BASE_URL}/tournaments/upcoming",
        params={
            "game": "VGC"
        },
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=20
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    tournaments = []


    for row in soup.find_all("tr"):

        cols = row.find_all("td")

        if len(cols) < 7:
            continue


        # ID e link
        name_link = cols[3].find("a")

        if not name_link:
            continue

        name = name_link.text.strip()

        href = name_link.get("href")

        tournament_id = href.split("/")[2]


        # Data timestamp
        date_element = cols[2].find("a")

        if not date_element:
            continue

        timestamp = int(
            date_element["data-time"]
        ) / 1000


        date = datetime.fromtimestamp(
            timestamp,
            tz=timezone.utc
        )


        # Organizzatore
        organizer = cols[4].text.strip()


        # Registrazioni
        registration_text = cols[6].text.strip()

        players = 0
        max_players = None

        if "/" in registration_text:
            current, maximum = registration_text.split("/")

            players = int(
                current.strip()
            )

            max_players = int(
                maximum.split()[0]
            )

        else:
            players = int(
                registration_text.split()[0]
            )


        tournaments.append({

            "id": tournament_id,

            "name": name,

            "organizer": organizer,

            "date": date.isoformat(),

            "players": players,

            "max_players": max_players,

            "url":
                f"{BASE_URL}{href}"

        })


    return tournaments
