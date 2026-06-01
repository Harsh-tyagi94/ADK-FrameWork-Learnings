# Google ADK Learning Projects

Demo and learning projects for Google AI/ML development.

## Setup

1. **Clone repository**

   ```bash
   git clone https://github.com/Harsh-tyagi94/ADK-FrameWork-Learnings.git
   cd google_adk
   ```

2. **Create virtual environment**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Mac/Linux
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Setup environment variables**
   - Copy `.env.example` → `.env` in each project folder
   - Add your API keys (Google, OpenRouter, Tavily)
   - Never commit `.env` files

5. **Run projects**
   ```bash
   cd first_agent
   python agent.py
   ```

## API Keys Needed

| Service              | Key                  | Where                                  |
| -------------------- | -------------------- | -------------------------------------- |
| Google Generative AI | `GOOGLE_API_KEY`     | https://aistudio.google.com/app/apikey |
| OpenRouter           | `OPENROUTER_API_KEY` | https://openrouter.ai/keys             |
| Tavily Search        | `TAVILY_API_KEY`     | https://tavily.com/dashboard           |

## Important

- **Never commit `.env` files** - they're ignored by `.gitignore`
- Copy `.env.example` → `.env` and add your actual keys locally only
- Each project may use different keys - check the `.env.example` in each folder

## Projects

- `adk_learning/` - Basic Google AI SDK learning
- `first_agent/` - First agent implementation
- `multiagent/` - Multi-agent setup
- `mcp/` - Model Context Protocol
- `openRouter_models/` - OpenRouter API
- `ollma_model_agent/` - Ollama integration
- `workflowagents/` - Workflow agents
- Other demo projects...

---

**Note**: These are learning/demo projects. For production, use proper secret management.
