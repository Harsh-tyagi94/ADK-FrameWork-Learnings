from google.adk.agents.llm_agent import Agent
from google.adk.agents import SequentialAgent, ParallelAgent

def make_translator_agent(lang_code, output_key):
    return Agent(
        name=f"Translator_{lang_code}",
        model='gemini-2.5-flash',
        instruction=f"Translate the user prompt into {lang_code}. "
                    "Return ONLY the translation text.",
        output_key=output_key,
    )

spanish=make_translator_agent("Spanish", "spanish_key")
french=make_translator_agent("french", "French_key")
german=make_translator_agent("German", "German_key")

parallel_translate = ParallelAgent(
    name='ParallelTranslate',
    sub_agents=[spanish, french, german],
    description='Generate localized marketing taglines for Spanish, French, and German audiences.'
)

merge_agent = Agent(
    model='gemini-2.5-flash',
    name='Merger_Agent',
    instruction='''Package the taglines neatly:
     **Spanish** {spanish_key}
     **French** {French_key}
     **German** {German_key}

     Return the response in the following JSON format:
     ```
     {
       "es": "tagline_text",
       "fr": "tagline_text",
       "de": "tagline_text"
     }
     ```
    ''',
    output_key='merged_translation',
)


sequential_pipeline = SequentialAgent(
    name='sequentialPipeline',
    sub_agents=[parallel_translate, merge_agent],
)


root_agent = sequential_pipeline
