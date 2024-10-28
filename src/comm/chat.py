import json

import genai_wrapper
from genai_wrapper import (
    Config,
    ChatObject
)
from .base_comm import BaseComm

class Chat(BaseComm):
    def __init__(self, llm_model: str) -> None:
        self.llm_model = llm_model
        super().__init__(
            cu=f"{Config.AI.AI_URLTYPE[0]}?{Config.AI.AI_VER}",
            dp=genai_wrapper.central_config["gen_ai"][llm_model]["deploymentid"],
            pm=Config.AI.AI_PARAMS | genai_wrapper.central_config["gen_ai"][llm_model]["parameters"]
        )

    def query(self, chat_object: ChatObject) -> ChatObject:
        payload = { "messages": chat_object._get_message_() }
        if not genai_wrapper.central_config["gen_ai"][self.llm_model]["model_name"].lower().startswith("gpt"):
            payload = { "model": genai_wrapper.central_config["gen_ai"][self.llm_model]["model_name"], "stream": False  } | payload        
        return chat_object._process_output_(
            super().query( payload )
        )