from pathlib import Path
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters
from google.adk.agents.llm_agent import Agent

CALCULATOR_MCP_PROMPT = """
You are an intelligent assistant capable of performing various math operations using a connected calculator toolset.

Your tools include:
- `basic_math`: Handles addition, subtraction, multiplication, and division.
- `power`: Calculates exponentiation.
- `modulus`: Computes the remainder of a division operation.
- `square_root`: Returns the square root of a given number.

Usage Principles:
- **Always respond using the appropriate tool** based on user input.
- If user says: "What is 5 plus 3?" → use `basic_math` with operation `add`.
- If user says: "What's 7 raised to the power 2?" → use `power`.
- If user doesn't specify values clearly, ask a short clarifying question.
- **Be concise** in presenting results. Format answer like: "Answer: 64"
- Handle errors gracefully and explain what went wrong.
"""

# Dynamically compute the absolute path to your MCP server
PATH_TO_YOUR_MCP_SERVER_SCRIPT = str((Path(__file__).parent / "server.py").resolve())

root_agent = Agent(
    model='gemini-2.5-flash',
    name='calculator_mcp_client_agent',
    description='A helpful assistant for user questions.',
    instruction=CALCULATOR_MCP_PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command="python3",
                    args=[PATH_TO_YOUR_MCP_SERVER_SCRIPT],
                )
            )
            # Optional: you can filter tools like tool_filter=["basic_math"]
        )
    ],
)
