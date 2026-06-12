from crewai import Agent, Crew, Process, Task
# Import the tool class wrapper
from src.tools.agricultural_observatory import KenyaAgriculturalObservatoryTool

class UjimaAgentPride:
    def assemble_pride(self, input_data):
        
        # Instantiate the tool object properly
        observatory_tool = KenyaAgriculturalObservatoryTool()

        # 1. Scout Agent (Equipped with the agricultural observatory tool)
        scout = Agent(
            role="Ujima Contextual Scout",
            goal="Analyze localized regional agricultural context, harvesting data, and climate realities.",
            backstory="An expert in East African smallholder logistics, specializing in local harvest patterns.",
            tools=[observatory_tool],  # Instantiated instance makes Pydantic happy
            allow_delegation=False,
            verbose=True
        )

        # 2. Guardian Agent (Enforces safety regulations)
        guardian = Agent(
            role="Ujima Safety Guardian",
            goal="Ensure evaluation aligns perfectly with DPA 2022 principles and fair-lending guardrails.",
            backstory="A dedicated compliance officer protecting marginalized applicant demographics from automated proxy discrimination.",
            tools=[],
            allow_delegation=False,
            verbose=True
        )

        # 3. Hunter Agent (Compiles final decisioning brief)
        hunter = Agent(
            role="Ujima Summary Hunter",
            goal="Synthesize scout insights and guardian checks into a dignified, actionable empowerment brief.",
            backstory="An expert financial analyst dedicated to community-centric funding models.",
            tools=[],
            allow_delegation=False,
            verbose=True
        )

        # Define basic tasks for the workflow execution loop
        scout_task = Task(
            description=f"Assess localized harvest cycles and baseline cash flow indicators for: {input_data}",
            expected_output="A contextual profile mapping current regional market performance.",
            agent=scout
        )

        guardian_task = Task(
            description="Audit the scout's data markers to ensure zero demographic proxy elements are included.",
            expected_output="A cleared safety compliance log.",
            agent=guardian
        )

        hunter_task = Task(
            description="Compile the final synthesized community briefing, applying the Dignity Filter language standards.",
            expected_output="A final dignified applicant appraisal report.",
            agent=hunter
        )

        # Wire them up into a cooperative Crew
        ujima_crew = Crew(
            agents=[scout, guardian, hunter],
            tasks=[scout_task, guardian_task, hunter_task],
            process=Process.sequential,
            verbose=True
        )

        return ujima_crew.kickoff()