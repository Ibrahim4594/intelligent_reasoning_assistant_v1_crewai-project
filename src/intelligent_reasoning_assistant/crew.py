import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	DallETool
)



@CrewBase
class IntelligentReasoningAssistantCrew:
    """IntelligentReasoningAssistant crew"""

    
    @agent
    def intelligent_reasoning_assistant(self) -> Agent:
        
        return Agent(
            config=self.agents_config["intelligent_reasoning_assistant"],
            tools=[DallETool()],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def intelligent_assistance_and_reasoning(self) -> Task:
        return Task(
            config=self.tasks_config["intelligent_assistance_and_reasoning"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the IntelligentReasoningAssistant crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
