from crewai_tools import SerperDevTool
from crewai.tools import BaseTool

class InternetSearchTool(BaseTool):
    """Ferramenta de pesquisa na internet usando SerperDevTool."""
    name = "Internet Search Tool"
    description = "Busca informações na web sobre um tópico usando SerperDevTool."

    def __init__(self, max_results=5):
        super().__init__()
        self.serper_tool = SerperDevTool()
        self.serper_tool.n_results = max_results  # Define o número de resultados retornados

    def _run(self, topic: str) -> str:
        try:
            results = self.serper_tool.search(topic)
            summaries = [f"- {result['title']}: {result['link']}" for result in results]
            return f"Resultados da busca sobre {topic}:\n" + "\n".join(summaries)
        except Exception as e:
            return f"Erro durante a busca: {str(e)}"

# Instanciar a ferramenta
search_tool = InternetSearchTool()
