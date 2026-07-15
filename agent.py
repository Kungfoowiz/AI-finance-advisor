from google.adk.agents.llm_agent import Agent
from tool_finance import analyse_stock

root_agent = Agent(
    model='gemini-3.5-flash',
    name='finance_advisor',
    description='An AI finance advisor.',
    instruction="""Ask the investor, if they want to analyse a specific stock or give them a comparative analysis 3 random stocks.
        Always use the 'analyse_stock' tool when a specific stock needs analysis.""",
    tools=[analyse_stock]
)
