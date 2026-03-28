import yaml

with open("./config.yaml", "r") as file:
    models_config = yaml.safe_load(file)

# OpenAI
OPENAI_API_KEY = models_config["openai"]["api_key"]
OPENAI_MODEL = models_config["openai"]["model"]

# Google GenAI
GOOGLE_GEN_AI_API_KEY = models_config["google_genai"]["api_key"]
GOOGLE_MODEL = models_config["google_genai"]["model"]

# Anthropic
ANTHROPIC_API_KEY = models_config["anthropic"]["api_key"]
ANTHROPIC_MODEL = models_config["anthropic"]["model"]

# Ollama Cloud
OLLAMA_CLOUD_API_KEY = models_config["ollama_cloud"]["api_key"]
OLLAMA_CLOUd_MODEL = models_config["ollama_cloud"]["model"]