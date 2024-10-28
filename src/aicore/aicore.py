import genai_wrapper
from genai_wrapper import AICoreV2Client

class AICore:
    def init() -> None:
        genai_wrapper.ai_core_client = AICoreV2Client(
            base_url=genai_wrapper.central_config["ai_core"]["secret"]["url"],
            auth_url=genai_wrapper.central_config["ai_core"]["secret"]["serviceurls"]["AI_API_URL"] + ( "/oauth/token" if "/oauth/token" not in genai_wrapper.central_config["ai_core"]["secret"]["serviceurls"]["AI_API_URL"] else "" ),
            client_id=genai_wrapper.central_config["ai_core"]["secret"]["clientid"],
            client_secret=genai_wrapper.central_config["ai_core"]["secret"]["clientsecret"]
        )

    def get_client() -> AICoreV2Client:
        return genai_wrapper.ai_core_client

