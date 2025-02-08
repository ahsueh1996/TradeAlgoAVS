from collections.abc import Callable
from json import dumps

import wspy
from pydantic import BaseModel

from cdp_agentkit_core.actions.finance.wealthsimple.action import WealthsimpleAction

ACCOUNT_LOGIN_PROMPT = """
This tool will help the Wealthsimple client submit the user's email and password.

A few status responses are possible.
"OK": Full success. The cient is now fully authenticated and can begin trading or viewing account details.
"OTP": Half success. The email and password credentials are correct but there is a one time passcode sent to the user's phone that they need to now provide. Hint, use the account_otp action next.
"BAD_CREDS": Failure. The email and password is incorrect. The user can try to supply the email and password again.
"UNKNOWN,BAD_CREDS": Failure. similar to the above but maybe some uncaught errors exists.

You may answer in a natural language way to help the user get logged in. 
The usual flow on a new browser is account_login, receive "OTP" status, account_otp, receive "OK" status.
Sometimes the flow may be expedited. Account_login, receive "OK" status immediately.
"""


class AccountLoginInput(BaseModel):
    """Input argument schema for WS account login action."""


def account_login(client: wspy.Client, email, password) -> str:
    """
    Logs into the specified account

    Returns the current login status
    """
    message = ""

    client.login(email, password)

    return client.login_status


class AccountLoginAction(WealthsimpleAction):

    name: str = "account_login"
    description: str = ACCOUNT_LOGIN_PROMPT
    args_schema: type[BaseModel] | None = AccountLoginInput
    func: Callable[..., str] = account_login
