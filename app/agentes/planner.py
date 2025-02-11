from crewai import Agent
from crewai_tools import SerperDevTool  # Importando a ferramenta de busca diretamente

# Instancia o SerperDevTool e define o número de resultados desejado
serper_tool = SerperDevTool()
serper_tool.n_results = 5  # Limite de resultados retornados por busca

class Planner(Agent):
    """Classe para o agente Planejador de conteúdo."""
    def __init__(self):
        super().__init__(
            role="Planejador de conteúdo",
            goal="Planeje conteúdo envolvente e factualmente preciso sobre {topic}. Use a web para obter informações relevantes.",
            backstory="Você está planejando um artigo para o blog sobre o tópico: {topic}. "
                      "Você coleta informações que ajudam o público a aprender algo novo "
                      "e tomar decisões informadas. Seu trabalho é a base para "
                      "o redator de conteúdo escrever um artigo sobre este tópico.",
            allow_delegation=False,
            verbose=True,
            tools=[serper_tool]  # Integra a ferramenta de busca diretamente
        )

# Instancia o agente Planner
planner = Planner()
