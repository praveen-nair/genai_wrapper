# **********************************************************************
# Config file, required by the package.
# *DO NOT MODIFY THIS FILE*
# **********************************************************************
class Config:
    class AI:
        AI_REQH: list = [
            "Authorization",
            "AI-Resource-Group",
            "Content-Type"
        ]
        AI_URLTYPE: list = [
            "chat/completions",
            "embeddings"
        ]
        AI_VER: str = "api-version=2023-05-15"
        AI_PARAMS: dict = {
            "max_tokens": 256,
            "temperature": 0.0,
            "frequency_penalty": 0,
            "presence_penalty": 0,
            "stop": "null"
        }