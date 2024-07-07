from crewai import Task
from app.agentes.editor import editor

class Edit(Task):
    """Classe para a tarefa de edição de conteúdo."""
    def __init__(self):
        super().__init__(
            description=("Revise a postagem do blog fornecida para erros gramaticais e alinhamento com a voz da marca."),
            expected_output="Uma postagem de blog bem escrita em formato markdown, pronta para publicação, cada seção deve ter 2 ou 3 parágrafos.",
            agent=editor
        )

# Instanciar a tarefa
edit = Edit()
