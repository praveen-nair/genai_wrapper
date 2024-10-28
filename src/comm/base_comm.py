import requests
import json

import genai_wrapper
from genai_wrapper import Config, GenAIWrapperException

class BaseComm:
    def __init__( self, **kwargs: dict ) -> None:
        self.bu = genai_wrapper.central_config["ai_core"]["secret"]["url"]
        self.cu = kwargs["cu"]
        self.dp = kwargs["dp"]
        self.bt = genai_wrapper.ai_core_client.rest_client.get_token()
        self.rg = genai_wrapper.central_config["ai_core"]["resource_group"]
        self.pm = kwargs["pm"]

    def query(self: object, data: dict) -> dict:
        result = requests.post(
            f"{self.bu}/v2/inference/deployments/{self.dp}/{self.cu}",
            headers={k:v for k,v in zip(Config.AI.AI_REQH, [self.bt, self.rg, "application/json"])}, 
            data=json.dumps(data | self.pm)
        )
        if result.status_code == 200:
            return json.loads( result.content )
        else:
            raise GenAIWrapperException(f"http request error (code: {result.status_code}) -> {result.text}")
