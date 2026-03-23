---
name: freeUnlimited-websearch
description: Free web search using Tavily (preferred) or DuckDuckGo fallback.
---

# Free Unlimited Web Search

Search the web for free using DuckDuckGo - no API key or rate limits.

## Features
- **Tavily (preferred)**: Set `TAVILY_API_KEY` for richer, LLM-optimized search results (1,000 free credits/month at https://app.tavily.com)
- **DuckDuckGo (fallback)**: No API key required — used automatically when `TAVILY_API_KEY` is not set
- **Same output format**: Both providers return results with `title`, `href`, and `body` fields

## Requirements
- Python 3.8+
- `ddgs` package (`pip install ddgs`) — required for DuckDuckGo fallback
- `tavily-python` package (`pip install tavily-python`) — optional, for Tavily search

## Installation

1. Install dependencies in a Python environment:
   ```bash
   pip install ddgs tavily-python
   ```

2. Clone this skill to your openclaw skills directory:
   ```bash
   git clone https://github.com/YOUR_USERNAME/openclaw-skill-freeUnlimited-websearch ~/.openclaw/skills/freeUnlimited-websearch
   ```

3. (Optional) Set the `TAVILY_API_KEY` environment variable to enable Tavily search:
   ```bash
   export TAVILY_API_KEY="tvly-YOUR_API_KEY"
   ```

4. Update `search.py` shebang to point to your Python with dependencies installed:
   ```bash
   # Edit the first line of search.py to your python path, e.g.:
   #!/path/to/your/venv/bin/python
   ```

5. Enable the skill in `~/.openclaw/openclaw.json`:
   ```json
   {
     "skills": {
       "entries": {
         "freeUnlimited-websearch": {
           "enabled": true
         }
       }
     }
   }
   ```

6. Restart openclaw:
   ```bash
   openclaw gateway restart
   ```

## Usage
The skill is automatically invoked when OpenClaw needs to search the web for current information.

## Output
Returns JSON array of search results with `title`, `href`, and `body` fields.
