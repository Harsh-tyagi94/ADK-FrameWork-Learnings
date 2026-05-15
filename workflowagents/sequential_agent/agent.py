from google.adk.agents.llm_agent import Agent
from google.adk.agents import SequentialAgent

def make_translator_agent(lang_code, output_key):
    return Agent(
        name=f"Translator_{lang_code}",
        model='gemini-2.5-flash',
        instruction=f"Translate the user prompt into {lang_code}. "
                    "Return ONLY the translation text.",
        output_key=output_key,
    )

spanish=make_translator_agent("Spanish", "es")
french=make_translator_agent("french", "fr")
german=make_translator_agent("German", "de")

sequential_agent = SequentialAgent(
    name='sequentialTranslate',
    sub_agents=[spanish, french, german],
    description='Run three translation agents in sequence.'
)

merge_agent = Agent(
     name="Merger",
     model='gemini-2.5-flash',
     instruction=(
         "Package the translations neatly:\n"
         "**Spanish:** {es}\n**French:** {fr}\n**German:** {de}"
         "\nReturn exactly that block."
     )
)

sequential_pipeline = SequentialAgent(
    name='sequentialPipeline',
    sub_agents=[sequential_agent, merge_agent],
)


root_agent = sequential_pipeline
