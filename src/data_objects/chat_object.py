import json

from genai_wrapper import GenAIWrapperException

class ChatObject:
    def __init__(self) -> None:
        self.messages = [
            {
                "role": "user",
                "content": ""
            }
        ]

    def _get_message_(self) -> list:
        return self.messages
    
    def _process_output_(self, output: str) -> None:
        self._response_ = output
        try:
            self._message: dict = output["choices"][0]["message"]
            self._usage: dict = output["usage"]
        except:
            raise GenAIWrapperException(f"Message does not contain the correct response.\n{self._response_}")
        
        return self

    def add_role(self, role: str, content: str, append: bool=False) -> None:
        if any(map(lambda message: message['role'] == 'user', self.messages)):
            for message in self.messages:
                if message['role'] == 'user':
                    message['content'] = content if not append else message['content'] + content
        else:
            self.messages.append({"role": role, "content": content})

    def add_message(self, content: str, append: bool=False) -> None:
        self.add_role("user", content, append)

    def get_answer(self) -> str:
        try:
            return self._message["content"]
        except:
            raise GenAIWrapperException(f"No query has been made to llm or the response was malformed!")

    def get_usage(self) -> dict:
        try:
            return self._usage
        except:
            raise GenAIWrapperException(f"No query has been made to llm or the response was malformed!")
