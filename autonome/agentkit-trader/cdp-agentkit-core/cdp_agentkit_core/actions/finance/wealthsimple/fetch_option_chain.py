from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_OPTION_CHAIN_PROMPT = """
This tool will help the fetch the raw options chain for a given security, expiry date and both the CALL or PUT side of the chain.

Success: The returned data will be in the form of a JSON object.
Failure: The returned data will be in the form of a JSON object with an error message.

You are able to use the details together with other details to create a custom report or to analyze the data.
Suggested useage. Resolve the security id by looking at what the user wants to know about.
NOTE: some securities may not have an options chain, so be sure to check if the security has an options chain before fetching it.
Then use this tool to fetch the options chain for a specific security on a specific expiry date.
Users will want to save time when they ask you to fetch details for a security, so it's generally the case
that they will need you to use this tool more than once in a single reply back to them so that you can automate
the process of fetching the details for multiple expiry dates and comparing them.
"""


class FetchOptionChainInput(BaseModel):
    """Input argument schema for WS account login action."""
    security_id: str = Field(
        ...,
        description="The ws security id, unique to wealthsimple that the user wants to fetch details for. NOTE: this is not the ticker symbol, it's the unique ws identifier that should be resolved by you as the agent.",
    )
    expiry: str = Field(
        ...,
        description="The expiry date of the option in the format YYYY-MM-DD where MM and DD are NOT zero padded.",
    )



def fetch_option_chain(client: wspy.Client, security_id, expiry) -> str:

    call_response = client.fetch_option_chain(security_id, expiry, "CALL")
    put_response = client.fetch_option_chain(security_id, expiry, "PUT")

    return dumps({
        "call": call_response,
        "put": put_response
    })


class FetchOptionChainAction(WealthsimpleAction):

    name: str = "fetch_option_chain"
    description: str = FETCH_OPTION_CHAIN_PROMPT
    args_schema: type[BaseModel] | None = FetchOptionChainInput
    func: Callable[..., str] = fetch_option_chain
