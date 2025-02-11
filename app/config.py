import os

class Config:
    """Classe de configuração para a aplicação Flask."""
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_MODEL_NAME = 'gpt-4o-mini-2024-07-18'
    CORS_HEADERS = 'Content-Type'
