from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_OPTION_EXPIRY_PROMPT = """
This tool will help the fetch the raw option expiry dates for a given security. All currently available expiry dates will be returned.

Success: The returned data will be in the form of a JSON object.
Failure: The returned data will be in the form of a JSON object with an error message.

You are able to use the details together with other details to create a custom report or to analyze the data.
Suggested useage. Resolve the security id by looking at what the user wants to know about.
NOTE: some securities may not have an options chain, so be sure to check if the security has an options chain before fetching it.
This tool will give an idea of what expiry dates are available for a given security.
Users will want to save time when they ask you to, say, compare the option chain from different expiry dates to find the best one.
Use this tool to fetch the expiry dates for a specific security.
"""


class FetchOptionExpiryInput(BaseModel):
    """Input argument schema for WS account login action."""
    security_id: str = Field(
        ...,
        description="The ws security id, unique to wealthsimple that the user wants to fetch details for. NOTE: this is not the ticker symbol, it's the unique ws identifier that should be resolved by you as the agent.",
    )



def fetch_option_expiry(client: wspy.Client, security_id) -> str:

    response = client.fetch_option_expiry(security_id)

    return response


class FetchOptionExpiryAction(WealthsimpleAction):

    name: str = "fetch_option_expiry"
    description: str = FETCH_OPTION_EXPIRY_PROMPT
    args_schema: type[BaseModel] | None = FetchOptionExpiryInput
    func: Callable[..., str] = fetch_option_expiry
