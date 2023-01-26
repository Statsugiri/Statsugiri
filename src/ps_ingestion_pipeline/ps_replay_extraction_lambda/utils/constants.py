import os

CURR_VGC_FORMAT = "gen9vgc2023series2"
VALID_FORMATS = [
    CURR_VGC_FORMAT,
    "gen9ou",
]

EVENT_FORMAT_KEY = "format"
BUCKET_KEY_FIELD = "bucket_key"
BUCKET_NAME_FIELD = "bucket_name"
NUM_USERS_TO_PULL = 100
MAX_USERS = 500
REPLAY_BASE_URL = "https://replay.pokemonshowdown.com/"
REQUEST_TIMEOUT = 2  # [seconds]
REPLAYS_BUCKET_NAME = os.environ.get("REPLAYS_BUCKET_NAME")
KEY_DELIMITER = "#"
