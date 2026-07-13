from datetime import datetime, timedelta
import pytz


def filter_tournaments(tournaments, config):

    timezone = pytz.timezone(
        config["timezone"]
    )

    now = datetime.now(timezone)

    limit_date = now + timedelta(
        days=config["days_ahead"]
    )

    result = []

    for tournament in tournaments:

        start = tournament.get("date")

        if not start:
            continue

        start_time = datetime.fromisoformat(
            start.replace("Z", "+00:00")
        )

        start_time = start_time.astimezone(
            timezone
        )

        # filtro giorni
        if start_time < now or start_time > limit_date:
            continue

        # filtro orario
        hour = start_time.hour

        if not (
            config["start_hour"]
            <= hour
            < config["end_hour"] + 1
        ):
            continue


        players = tournament.get(
            "players",
            0
        )

        if players < config["min_players"]:
            continue


        result.append(tournament)


    return sorted(
        result,
        key=lambda x: x["date"]
    )
