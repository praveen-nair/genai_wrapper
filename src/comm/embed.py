import genai_wrapper
from genai_wrapper import Config
from .base_comm import BaseComm

class Embeddings(BaseComm):
    def __init__( self, llm_model: str ) -> None:
        super().__init__(
            cu=f"{Config.AI.AI_URLTYPE[1]}?{Config.AI.AI_VER}",
            dp=genai_wrapper.central_config["gen_ai"][llm_model]["deploymentid"],
            pm={}
        )

    def query( self, text ):
        return super().query( { "input": text } )["data"][0]["embedding"]