from google.adk.agents.llm_agent import Agent
import dotenv
from google.adk.models.lite_llm import LiteLlm
import os

dotenv.load_dotenv()
openrouter_model = LiteLlm(model='openrouter/openai/gpt-oss-120b:free',
                           api_key=os.getenv('OPENROUTER_API_KEY'))

root_agent = Agent(
    model=openrouter_model,
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
)
