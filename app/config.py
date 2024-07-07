import os

class Config:
    """Classe de configuração para a aplicação Flask."""
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    OPENAI_MODEL_NAME = 'gpt-3.5-turbo'
    CORS_HEADERS = 'Content-Type'
