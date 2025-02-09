from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_ACTIVITIES_PROMPT = """
This tool will help the Wealthsimple client fetch the raw activities for a given account.

Success: The returned data will be in the form of a JSON object.
Failure: The returned data will be in the form of a JSON object with an error message.

You are able to use the activities to create a custom report or to analyze the data.
"""


class FetchActivitiesInput(BaseModel):
    """Input argument schema for WS account login action."""
    ws_account_id: str = Field(
        ...,
        description="The ws_account_id that the user wants to fetch activities for.",
    )



def fetch_activities(client: wspy.Client, ws_account_id) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    return client.fetch_activities(ws_account_id)


class FetchActivitiesAction(WealthsimpleAction):

    name: str = "fetch_activities"
    description: str = FETCH_ACTIVITIES_PROMPT
    args_schema: type[BaseModel] | None = FetchActivitiesInput
    func: Callable[..., str] = fetch_activities
