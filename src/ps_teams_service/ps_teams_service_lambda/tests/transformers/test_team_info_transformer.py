import pytest
import boto3
from unittest.mock import MagicMock
from transformers.team_info_transformers import transform_to_get_team_response
from data.get_team_response import GetTeamResponse
from data.team_info import TeamInfo

TEST_TEAM_ID = "1234"
TEST_SNAPSHOT_DATE = "2023-04-03"
TEST_FORMAT_ID = "TEST_FORMAT"
TEST_SNAPSHOT_DATE_COMPOSITE = TEST_FORMAT_ID + "#" + TEST_SNAPSHOT_DATE
TEST_PKMN_TEAM = ["a", "b", "c", "d", "e", "f"]
TEST_RATING = 1602
TEST_REPLAY_ID = "REPLAY_ID"
TEST_REPLAY_UPLOAD_DATE = "REPLAY_UPLOAD_DATE"


def init_mock_query_response():
    return {
        "Count": 1,
        "Items": [
            {
                "team_id": {"S": TEST_TEAM_ID},
                "format_snapshot_date_composite": {"S": TEST_SNAPSHOT_DATE_COMPOSITE},
                "pkmn_team": {"SS": TEST_PKMN_TEAM},
                "rating": {"N": TEST_RATING},
                "replay_id": {"S": TEST_REPLAY_ID},
                "replay_upload_date": {"S": TEST_REPLAY_UPLOAD_DATE},
            }
        ],
    }


def init_mock_get_team_response():
    return GetTeamResponse(
        TEST_FORMAT_ID,
        TEST_SNAPSHOT_DATE,
        TeamInfo(
            TEST_TEAM_ID,
            TEST_PKMN_TEAM,
            TEST_RATING,
            TEST_REPLAY_ID,
            TEST_REPLAY_UPLOAD_DATE,
        ),
    )


def test_transform_get_team_by_id_to_response_happy_path():
    response = transform_to_get_team_response(init_mock_query_response())
    assert response == init_mock_get_team_response()
