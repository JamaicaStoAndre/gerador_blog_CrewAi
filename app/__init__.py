from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app():
    """Função de fábrica para criar a aplicação Flask."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configurar CORS para permitir solicitações de qualquer origem
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Registrar as rotas
    with app.app_context():
        from .routes import bp
        app.register_blueprint(bp)

    return app
