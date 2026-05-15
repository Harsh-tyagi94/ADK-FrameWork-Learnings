from google.adk.agents.llm_agent import Agent
from google.adk.models.lite_llm import LiteLlm

ollama_agent = LiteLlm(model='ollama_chat/llama3.2')

root_agent = Agent(
    model=ollama_agent,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
