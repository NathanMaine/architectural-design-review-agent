import os


class LLMClient:
    """
    Minimal placeholder LLM client.
    """

    def __init__(self):
        self.api_key = os.getenv("LLM_API_KEY")

    def complete(self, prompt: str, **kwargs) -> str:
        raise NotImplementedError("Connect this stub to your LLM provider.")
