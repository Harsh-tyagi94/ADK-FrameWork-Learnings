from google.adk.agents.llm_agent import Agent
from pydantic import BaseModel, Field

class EmailContent(BaseModel):
    """Blueprint for email outputs"""
    subject: str = Field(
        description="Concise, descriptive subject line (5-10 words)"
    )
    body: str = Field(
        description="Formatted content with greeting, paragraphs, and signature"
    )

from datetime import date

class TodoItem(BaseModel):
    task: str = Field(description="Task name")
    due_date: str = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

root_agent = Agent(
    model='gemini-2.5-flash',
    name='todo_agent',
    description='A helpful assistant for user questions.',
    instruction="Generate todo items in exact JSON format",
    output_schema=TodoItem,
    output_key='todo'
)
