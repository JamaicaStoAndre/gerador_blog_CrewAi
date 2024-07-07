from crewai import Agent

class Planner(Agent):
    """Classe para o agente Planejador de conteúdo."""
    def __init__(self):
        super().__init__(
            role="Planejador de conteúdo",
            goal="Planeje conteúdo envolvente e factualmente preciso sobre {topic}",
            backstory="Você está planejando um artigo para o blog sobre o tópico: {topic}. "
                      "Você coleta informações que ajudam o público a aprender algo novo "
                      "e tomar decisões informadas. Seu trabalho é a base para "
                      "o redator de conteúdo escrever um artigo sobre este tópico.",
            allow_delegation=False,
            verbose=True
        )

# Instanciar o agente
planner = Planner()
