from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_SECURITY_PROMPT = """
This tool will help the fetch the raw details for a given security. It works with any security type, including stocks, options, and crypto.

Success: The returned data will be in the form of a JSON object.
Failure: The returned data will be in the form of a JSON object with an error message.

You are able to use the details together with other details to create a custom report or to analyze the data.
Suggested useage. Resolve the security id by looking at what the user wants to know about. 
Then use this tool to fetch details (like option greeks) for a specific security.
Users will want to save time when they ask you to fetch details for a security, so it's generally the case
that they will need you to use this tool more than once in a single reply back to them so that you can automate
the process of fetching the details for multiple securities and comparing them.
"""


class FetchSecurityInput(BaseModel):
    """Input argument schema for WS account login action."""
    security_id: str = Field(
        ...,
        description="The ws security id, unique to wealthsimple that the user wants to fetch details for. NOTE: this is not the ticker symbol, it's the unique ws identifier that should be resolved by you as the agent.",
    )



def fetch_security(client: wspy.Client, security_id) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    return client.fetch_security(security_id)


class FetchSecurityAction(WealthsimpleAction):

    name: str = "fetch_security"
    description: str = FETCH_SECURITY_PROMPT
    args_schema: type[BaseModel] | None = FetchSecurityInput
    func: Callable[..., str] = fetch_security
