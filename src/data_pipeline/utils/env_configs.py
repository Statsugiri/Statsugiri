import os

MONGOURI = os.environ.get("MONGOURI")
ENV = os.environ.get("ENV")
DB_CLUSTER_NAME = os.environ.get("DB_CLUSTER_NAME")
POKEMON_TEAMS_SNAPSHOTS_COLLECTION = os.environ.get(
    "POKEMON_TEAMS_SNAPSHOTS_COLLECTION"
)
POKEMON_USAGE_SNAPSHOTS_COLLECTION = os.environ.get(
    "POKEMON_USAGE_SNAPSHOTS_COLLECTION"
)
