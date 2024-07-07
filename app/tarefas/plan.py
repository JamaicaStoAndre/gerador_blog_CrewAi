from crewai import Task
from app.agentes.planner import planner

class Plan(Task):
    """Classe para a tarefa de planejamento de conteúdo."""
    def __init__(self):
        super().__init__(
            description=(
                "1. Priorize as últimas tendências, os principais participantes e notícias dignas de nota sobre {topic}.\n"
                "2. Identifique o público-alvo, considerando seus interesses e pontos problemáticos.\n"
                "3. Desenvolva um esboço de conteúdo detalhado, incluindo uma introdução, pontos-chave e um apelo à ação.\n"
                "4. Inclua palavras-chave de SEO e dados ou fontes relevantes."
            ),
            expected_output="Um documento abrangente de plano de conteúdo com um esboço, análise de público, palavras-chave e recursos de SEO.",
            agent=planner,
        )

# Instanciar a tarefa
plan = Plan()
