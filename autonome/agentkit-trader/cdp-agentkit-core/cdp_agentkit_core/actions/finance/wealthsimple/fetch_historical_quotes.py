from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel, Field

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

FETCH_HISTORICAL_PROMPT = """
This tool will help the fetch the raw historical quotes for a given security. It works with any security type, including stocks, options, and crypto.
You are able to use the details together with other details to create a custom report or to analyze the data.
Resolve the security id by looking at what the user wants to know about then use this tool to fetch the price movement.
Users will want to know the price movement for a security over a specific time period and know something qualitative about the security.
For instance, they will want to know if the security has been trending up or down, or if it has been volatile or stable, or if the stock is currently undervalued or overvalued.
Another use case is to compare the price movement of a security with another security to see which one has been performing better.
Another use case is to use this tool to fetch the underlying price movement of a security and use it with the option chain data to estimate the potential returns of an option.
"""


class FetchHistoricalInput(BaseModel):
    """Input argument schema for WS account login action."""
    security_id: str = Field(
        ...,
        description="The ws security id, unique to wealthsimple that the user wants to fetch details for. NOTE: this is not the ticker symbol, it's the unique ws identifier that should be resolved by you as the agent.",
    )
    timerange: str = Field(
        ...,
        description="The timerange for the historical data. This can ONLY be '1d', '1m', '3m', '1y' or '5y'. Use the most appropriate one for the user's needs.",
    )



def fetch_historical_quotes(client: wspy.Client, security_id, timerange) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    return client.fetch_historical_quotes(security_id, timerange)


class FetchHistoricalAction(WealthsimpleAction):

    name: str = "fetch_historical_quotes"
    description: str = FETCH_HISTORICAL_PROMPT
    args_schema: type[BaseModel] | None = FetchHistoricalInput
    func: Callable[..., str] = fetch_historical_quotes
