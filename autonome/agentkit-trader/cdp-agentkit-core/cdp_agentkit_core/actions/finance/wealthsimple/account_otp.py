from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

ACCOUNT_OTP_PROMPT = """
This tool will help the Wealthsimple client submit the user's one-time passcode (OTP).
It's usually a 6 digit code that they receive on their phone over text message (SMS).

A few status responses are possible.
"OK": Full success. The cient is now fully authenticated and can begin trading or viewing account details.
"BAD_OTP": Failure. The OTP is incorrect, the user can try again.
"UNKNOWN,BAD_OTP": Failure. similar to the above but maybe some uncaught errors exists.

You may answer in a natural language way to help the user get their OTP submitted. The goal is to see the "OK" status.
"""


class AccountOTPInput(BaseModel):
    """Input argument schema for WS account login action."""


def account_otp(client: wspy.Client, email, password) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    message = ""

    client.login(email, password)

    return client.login_status


class AccountLoginAction(WealthsimpleAction):

    name: str = "account_otp"
    description: str = ACCOUNT_OTP_PROMPT
    args_schema: type[BaseModel] | None = AccountOTPInput
    func: Callable[..., str] = account_otp
