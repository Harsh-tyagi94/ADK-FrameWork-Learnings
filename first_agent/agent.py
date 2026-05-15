from typing import Dict
from google.adk.agents import LlmAgent

def get_capital_city(country: str) -> str:
	capitals = {"france": "Paris", "japan": "Tokyo", "canada": "ottawa"}
	return capitals.get(country.lower(), f"Sorry, I don't know the capital of {country}.")

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Answer questions about capital cities.',
    instruction=(
	"You provide country capitals.\n"
	"when asked for capital, call get_capital_city(country).\n"
	"Resond concisely."
    ),
    tools=[get_capital_city],
)
