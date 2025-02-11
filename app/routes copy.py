from flask import Blueprint, request, jsonify, render_template, send_from_directory
import warnings
from crewai import Crew
from app.agentes import planner, writer, editor, tone_analyzer
from app.tarefas import plan, write, edit, analyze_tone_task
import os

warnings.filterwarnings('ignore')

# Definir o Blueprint para as rotas
bp = Blueprint('routes', __name__)

# Configurações de ambiente
# As chaves da API devem ser definidas nas variáveis de ambiente

# Inicializar a equipe com os agentes e tarefas
crew = Crew(
    agents=[planner, tone_analyzer, writer, editor],
    tasks=[plan, analyze_tone_task, write, edit],
    verbose=True
)

@bp.route('/')
def index():
    """Rota para servir a página inicial."""
    return render_template('index.html')

@bp.route('/favicon.ico')
def favicon():
    """Rota para servir o favicon."""
    return send_from_directory(os.path.join(bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@bp.route('/api/kickoff', methods=['POST'])
def kickoff():
    """Endpoint para iniciar o processo da equipe."""
    data = request.json
    topic = data.get('topic')
    posts = data.get('posts', [])

    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    # Passar as postagens para a tarefa analyze_tone_task
    inputs = {"topic": topic, "posts": posts}
    result = crew.kickoff(inputs=inputs)

    # Tratar o resultado para remover os marcadores markdown e espaços indesejados
    clean_result = result.raw.strip()  # Remove espaços em branco no início/fim
    clean_result = clean_result.lstrip("```markdown").rstrip("```").strip()

    # Converter CrewOutput para JSON serializável
    response_data = {
        "result": clean_result,
        "logs": result.logs if hasattr(result, 'logs') else None,
        "errors": result.errors if hasattr(result, 'errors') else None
    }

    return jsonify(response_data)



