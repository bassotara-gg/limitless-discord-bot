import json
import os


STATE_FILE = "state.json"


def load_state():

    if not os.path.exists(STATE_FILE):
        return {
            "posted": []
        }

    with open(
        STATE_FILE,
        "r",
        encoding="utf-8"
    ) as file:
        return json.load(file)



def save_state(state):

    with open(
        STATE_FILE,
        "w",
        encoding="utf-8"
    ) as file:
        json.dump(
            state,
            file,
            indent=4
        )



def is_posted(tournament_id):

    state = load_state()

    return tournament_id in state["posted"]



def mark_as_posted(tournament_id):

    state = load_state()

    if tournament_id not in state["posted"]:
        state["posted"].append(
            tournament_id
        )

    save_state(state)
