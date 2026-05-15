from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
load_dotenv()

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='''Answer user questions to the best of your knowledge
    You might have to answer questions about the user, their interests, and preferences.
    You can access the same for user {name} in the session state.
    and the data information is: {data},
    '''
)
