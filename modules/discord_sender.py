import os
import requests


def send_discord_message(tournaments):

    webhook = os.getenv("DISCORD_WEBHOOK")

    if not webhook:
        raise Exception(
            "DISCORD_WEBHOOK non trovato"
        )


    for t in tournaments:

        if t["max_players"]:
            players = (
                f'{t["players"]}/{t["max_players"]}'
            )
        else:
            players = str(t["players"])


        embed = {
            "title": f'🏆 {t["name"]}',
            "url": t["url"],
            "color": 15158332,

            "fields": [
                {
                    "name": "📅 Inizio torneo",
                    "value": (
                        f'<t:{t["discord_timestamp"]}:F>\n'
                        f'<t:{t["discord_timestamp"]}:R>'
                    ),
                    "inline": False
                },
                {
                    "name": "👥 Iscritti",
                    "value": players,
                    "inline": True
                },
                {
                    "name": "🏢 Organizzatore",
                    "value": t["organizer"],
                    "inline": True
                }
            ],

            "footer": {
                "text": "Limitless VGC Bot"
            }
        }


        response = requests.post(
            webhook,
            json={
                "username": "Limitless VGC Bot",
                "embeds": [embed]
            },
            timeout=20
        )

        response.raise_for_status()


    return True
