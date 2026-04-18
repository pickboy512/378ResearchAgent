from crewai import Agent, Task, Crew

research_task = Task(
    description="Explain the attack",
    agent=research_agent
)

response_task = Task(
    description="Give safety steps",
    agent=response_agent
)

crew = Crew(
    agents=[research_agent, response_agent],
    tasks=[research_task, response_task]
)

crew.kickoff()