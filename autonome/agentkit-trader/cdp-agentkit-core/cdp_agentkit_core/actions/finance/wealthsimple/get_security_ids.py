from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

GET_SECURITY_IDS_PROMPT = """
This tool will help get the security ids for some symbols. You can use this tool to resolve the security id for a given symbol.

Success: The returned data will be in the form of a JSON object.
Failure: None

You will use this tool when infering which security the user is talking about. For example, if the user says "fetch the details for AAPL", you will use this tool to resolve the security id for AAPL.
But the user might also say "fetch the details for the 2023 100 strike call option on AAPL", in which case you will need to resolve the security id for AAPL and then use it to fetch the details for the option.
The user might also be talking about sectors in general and not a specific security, in which case you will need to resolve the security id by first looking at the user's intent and then using this tool to resolve the security id for the symbols that appear in that sector.
For example, if the user says "fetch the details for the tech sector", you will need to resolve the security ids for all the symbols in the tech sector.
"""


class GetSecurityIDsInput(BaseModel):
    """Input argument schema for WS account login action."""


def get_security_ids(client: wspy.Client) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    return client.get_security_ids()


class FetchSecurityAction(WealthsimpleAction):

    name: str = "get_security_ids"
    description: str = GET_SECURITY_IDS_PROMPT
    args_schema: type[BaseModel] | None = GetSecurityIDsInput
    func: Callable[..., str] = get_security_ids
