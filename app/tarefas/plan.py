from crewai import Task
from app.agentes.planner import planner

# Define a tarefa de planejamento
plan = Task(
    description="""Use a ferramenta de busca na web para encontrar informações relevantes 
    sobre {topic}. As informações devem ser factualmente corretas e servir como base para 
    o redator escrever o artigo.""",
    expected_output="Um resumo com os pontos mais importantes encontrados na web sobre {topic}.",
    tools=planner.tools,  # Ferramenta de busca do planner (SerperDevTool)
    agent=planner  # Agente responsável pela tarefa
)
