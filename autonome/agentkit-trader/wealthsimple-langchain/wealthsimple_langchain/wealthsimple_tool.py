"""Tool allows agents to interact with the Wealthsimple API."""

from collections.abc import Callable
from typing import Any

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from pydantic import BaseModel

from wealthsimple_langchain.wealthsimple_api_wrapper import WealthsimpleApiWrapper


class WealthsimpleTool(BaseTool):  # type: ignore[override]
    """Tool for interacting with the Wealthsimple API."""
    # this is a general class to help us define WS tools.

    wealthsimple_api_wrapper: WealthsimpleApiWrapper
    name: str = ""
    description: str = ""
    args_schema: type[BaseModel] | None = None
    func: Callable[..., str]

    def _run(
        self,
        instructions: str | None = "",
        run_manager: CallbackManagerForToolRun | None = None,
        **kwargs: Any,
    ) -> str:
        """Use the Wealthsimple API to run an operation."""
        if not instructions or instructions == "{}":
            # Catch other forms of empty input that GPT-4 likes to send.
            instructions = ""
        if self.args_schema is not None:
            validated_input_data = self.args_schema(**kwargs)
            parsed_input_args = validated_input_data.model_dump()
        else:
            parsed_input_args = {"instructions": instructions}
        # here if a tool were to have the first kwarg to be the wspy.Client, the wrapper will handle the connection with the intantialized client
        return self.wealthsimple_api_wrapper.run_action(self.func, **parsed_input_args) 
    
