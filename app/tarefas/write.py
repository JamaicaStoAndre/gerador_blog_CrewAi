from crewai import Task
from app.agentes.writer import writer

class Write(Task):
    """Classe para a tarefa de escrita de conteúdo."""
    def __init__(self):
        super().__init__(
            description=(
                "1. Use o plano de conteúdo e a análise de tom e linguagem para criar uma postagem do blog sobre {topic}.\n"
                "2. Incorpore palavras-chave SEO naturalmente.\n"
                "3. As seções/legendas estão nomeadas corretamente de uma maneira envolvente.\n"
                "4. Certifique-se de que a postagem esteja estruturada com uma introdução envolvente, corpo perspicaz e uma conclusão resumida.\n"
                "5. Revise erros gramaticais e alinhamento com a voz da marca e com o tom das postagens.\n"
            ),
            expected_output="Uma postagem de blog bem escrita em formato markdown, pronta para publicação, cada seção deve ter 2 ou 3 parágrafos.",
            agent=writer,
        )

# Instanciar a tarefa
write = Write()
