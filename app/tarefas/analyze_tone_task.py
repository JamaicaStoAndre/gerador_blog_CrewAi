from crewai import Task
from app.agentes.tone_analyzer import tone_analyzer

class AnalyzeToneTask(Task):
    """Classe para a tarefa de análise de tom."""
    def __init__(self):
        super().__init__(
            description=(
                "Analise o tom e a linguagem das seguintes postagens. Sua análise deve destacar o humor geral, o estilo e quaisquer padrões notáveis na linguagem. "
                "Esta análise será utilizada pelo escritor de conteúdo para ajustar o tom e a linguagem do novo texto."
            ),
            expected_output='Um relatório detalhado sobre o tom e a linguagem usados nas postagens.',
            tools=[],  # Não estamos usando ferramentas específicas
            agent=tone_analyzer,
            async_execution=False
        )

# Instanciar a tarefa
analyze_tone_task = AnalyzeToneTask()
