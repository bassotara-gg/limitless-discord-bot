import os
import requests


BASE_URL = "https://api.limitlesstcg.com"


def get_vgc_tournaments():
    """
    Recupera i tornei VGC da Limitless.
    """

    headers = {}

    api_key = os.getenv("LIMITLESS_API_KEY")

    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    response = requests.get(
        f"{BASE_URL}/tournaments",
        params={
            "game": "VGC"
        },
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    return response.json()
