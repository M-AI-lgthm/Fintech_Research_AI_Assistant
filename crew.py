from crewai import Crew

from agents.research_specialist import research_agent
from agents.fintech_analyst import fintech_analyst
from agents.reporting_specialist import reporting_agent
from tasks.research_task import research_task
from tasks.analysis_task import analysis_task
from tasks.reporting_task import reporting_task


research_crew = Crew(
    agents=[
        research_agent,
        fintech_analyst,
        reporting_agent,
    ],
    tasks=[
        research_task,
        analysis_task,
        reporting_task,
    ],
    verbose=True
)
