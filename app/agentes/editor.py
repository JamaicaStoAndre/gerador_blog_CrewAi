from crewai import Agent

class Editor(Agent):
    """Classe para o agente Editor."""
    def __init__(self):
        super().__init__(
            role="Editor",
            goal="Editar uma determinada postagem do blog para alinhá-la com o estilo de escrita da organização.",
            backstory="Você é um editor que recebe uma postagem no blog do redator de conteúdo. "
                      "Seu objetivo é revisar a postagem do blog para garantir que siga as melhores práticas jornalísticas, "
                      "forneça pontos de vista equilibrados ao fornecer opiniões ou afirmações, e também evite grandes temas polêmicos "
                      "ou opiniões quando possível.",
            allow_delegation=False,
            verbose=True
        )

# Instanciar o agente
editor = Editor()
