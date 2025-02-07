from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

ACCOUNT_LOGIN_PROMPT = """
This tool will help the WS client get authenticated for a user context.

A successful response will return a message with the api response as a json payload:
    {"data": {"state": "awaiting 2fa/logged in", "name": "TaAVS AgentKit", "username": "TaAVSAgentKit"}}

A failure response will return a message with the tweepy client api request error:
    Error retrieving authenticated user account: 429 Too Many Requests


"""


class AccountLoginInput(BaseModel):
    """Input argument schema for WS account login action."""


def account_login(client: wspy.Client) -> str:
    """Get the authenticated Twitter (X) user account details.

    Args:
        client (tweepy.Client): The Twitter (X) client used to authenticate with.

    Returns:
        str: A message containing account details for the authenticated user context.

    """
    message = ""

    try:
        response = client.get_me()
        data = response["data"]
        data["url"] = f"https://x.com/{data['username']}"

        message = (
            f"""Successfully retrieved authenticated user account details:\n{dumps(response)}"""
        )
    except tweepy.errors.TweepyException as e:
        message = f"Error retrieving authenticated user account details:\n{e}"

    return message


class AccountLoginAction(WealthsimpleAction):
    """Twitter (X) account details action."""

    name: str = "account_details"
    description: str = ACCOUNT_LOGIN_PROMPT
    args_schema: type[BaseModel] | None = AccountLoginInput
    func: Callable[..., str] = account_details
