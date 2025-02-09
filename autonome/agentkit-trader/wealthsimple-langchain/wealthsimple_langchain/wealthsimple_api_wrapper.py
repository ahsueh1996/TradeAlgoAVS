"""Util that calls Wealthsimple API."""

import inspect
from collections.abc import Callable
from typing import Any

import wspy
from langchain_core.utils import get_from_dict_or_env
from pydantic import BaseModel, model_validator


class WealthsimpleApiWrapper(BaseModel):
    """Wrapper for Wealthsimple API."""

    client: Any | None = None
    ws_email: str
    ws_password: str
    ws_account_id: str

    @model_validator(mode="before")
    @classmethod
    def validate_environment(cls, values: dict) -> Any:
        """
        You can use this to create a client.
        You can also pass in overriding values to help create the client.
        """

        """Validate that Wealthsimple access token, token secret, and wspy exists in the environment."""
        # actually we don't want to have these. The operator is generic therefore we will pull these secrets later when necessary.
        ws_email = get_from_dict_or_env(values, "ws_email", "WS_EMAIL")
        ws_password = get_from_dict_or_env(values, "ws_password", "WS_PASSWORD")
        ws_account_id = get_from_dict_or_env(values, "ws_password", "WS_ACCOUNT_ID")

        try:
            import wspy
        except Exception:
            raise ImportError(
                "wspy Wealthsimple SDK is not installed. "

                "Please ensure the 'wealtsimple-core' package is installed or properly depended on in the poetry.toml file."
            ) from None

        client = wspy.Client()  # Easiest client. 

        values["client"] = client
        values["email"] = ws_email
        values["password"] = ws_password
        values["account_id"] = ws_account_id

        return values

    def run_action(self, func: Callable[..., str], **kwargs) -> str:
        # this is a generic piece of code we inherited from the cdp twitter wrapper.
        # basically it take your kwargs and checks if it should be a self call... we've alerady initialized
        # a client so it should use that client context to do everything.
        """Run a Wealthsimple Action."""
        func_signature = inspect.signature(func)
        first_kwarg = next(iter(func_signature.parameters.values()), None)

        # HACK
        if 'email' in kwargs and 'password' in kwargs:
            print(f">>>>>>> [{str(func)}] Replacing login email and password with default .env secret!! <<<<<<<")
            kwargs['email'] = self.ws_email
            kwargs['password'] = self.ws_password
        if 'ws_account_id' in kwargs:
            print(f">>>>>>> [{str(func)}] Replacing ws_account_id with default .env secret!! <<<<<<<")
            kwargs['email'] = self.ws_account_id

        if first_kwarg and first_kwarg.annotation is wspy.Client:
            return func(self.client, **kwargs)
        else:
            return func(**kwargs)
