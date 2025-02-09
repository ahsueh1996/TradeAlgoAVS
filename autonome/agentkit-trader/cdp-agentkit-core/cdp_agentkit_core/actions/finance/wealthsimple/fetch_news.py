from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_NEWS_PROMPT = """
This tool will help the fetch any available news about a given security.

Success: The returned data will be in the form of a JSON object. It could be empty if there is no news available.
Failure: The returned data will be in the form of a JSON object with an error message.

You are able to cite the news data to give reasons for your trading decisions or suggestions or explanations to the user about the security price movements.
"""


class FetchNewsInput(BaseModel):
    """Input argument schema for WS account login action."""
    security_id: str = Field(
        ...,
        description="The ws security id, unique to wealthsimple that the user wants to fetch details for. NOTE: this is not the ticker symbol, it's the unique ws identifier that should be resolved by you as the agent.",
    )



def fetch_news(client: wspy.Client, security_id) -> str:

    response = client.fetch_news(security_id)

    return response


class FetchNewsAction(WealthsimpleAction):

    name: str = "fetch_news"
    description: str = FETCH_NEWS_PROMPT
    args_schema: type[BaseModel] | None = FetchNewsInput
    func: Callable[..., str] = fetch_news
