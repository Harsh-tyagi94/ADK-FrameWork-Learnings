from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent
import dotenv

dotenv.load_dotenv()

sessions_service_in_memory = InMemorySessionService()
initial_state = {
    "name": "harsh",
    "data": '''
    I am Harsh, working hard to became AI fullStack engineer,
    i am currently learning google ADK and distributed systems and love doing Compitative Programming
    '''
}

APP_NAME = "answer Agent"
USER_ID = "Harsh"
SESSION_ID = "Harsh_session"

import asyncio

async def main():
    current_session = await sessions_service_in_memory.create_session(
        session_id=SESSION_ID,
        user_id=USER_ID,
        app_name=APP_NAME,
        state=initial_state
    )

    print(f"Session created with ID: {SESSION_ID}")

    created_sessions = await(sessions_service_in_memory.list_sessions(
        user_id=USER_ID,
        app_name=APP_NAME))
    print(f"Created sessions: {created_sessions}")

    runner = Runner(
        agent = root_agent,
        session_service = sessions_service_in_memory,
        app_name= APP_NAME
    )


    new_message = types.Content(
        role = 'user',
        parts = [types.Part(text='What is user currently learning?')]
    )


    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                print("Final response:", event.content.parts[0].text)



asyncio.run(main())
