from PyQt6.QtCore import QThread, pyqtSignal
from ...db import action



class ModelChatWorker(QThread):
    completed = pyqtSignal(object)

    def __init__(self, chat_client, provider: str, message: str):
        super().__init__()
        self.chat_client = chat_client
        self.provider = provider
        self.message = message

    def run(self):
        try:
            provider_map = {
                "OpenAI": self.chat_client.with_openai_model,
                "Google": self.chat_client.with_google_genai_model,
                "Anthropic": self.chat_client.with_anthropic_model,
                "Ollama Cloud": self.chat_client.with_ollama_cloud_model,
            }
            method = provider_map.get(self.provider)
            if method is None:
                self.completed.emit((False, "Please select a provider first."))
                return

            result = method(self.message)
            self.completed.emit(result)
        except Exception as e:
            self.completed.emit((False, str(e)))
