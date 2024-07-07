from crewai import Agent

class ToneAnalyzer(Agent):
    """Classe para o agente Analisador de Tom."""
    def __init__(self):
        super().__init__(
            role='Tone Analyzer',
            goal='Analisar o tom e a linguagem de uma série de postagens',
            verbose=True,
            memory=True,
            backstory=(
                "Você tem um olhar aguçado para entender as nuances da linguagem e do tom. "
                "Você consegue discernir o humor e o estilo do conteúdo com grande precisão."
            ),
            tools=[],  # Não estamos usando ferramentas específicas
            allow_delegation=False
        )

# Instanciar o agente
tone_analyzer = ToneAnalyzer()
