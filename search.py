#!/usr/bin/env python3
# search.py - Web search for OpenClaw (Tavily or DuckDuckGo)
# Update the shebang above to point to a Python environment with 'ddgs' (and optionally 'tavily-python') installed
import sys
import json
import os

TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

def _search_tavily(query):
    from tavily import TavilyClient
    client = TavilyClient(api_key=TAVILY_API_KEY)
    response = client.search(query=query, max_results=5)
    # Normalize to match DuckDuckGo schema: title, href, body
    results = []
    for r in response.get("results", []):
        results.append({
            "title": r.get("title", ""),
            "href": r.get("url", ""),
            "body": r.get("content", ""),
        })
    return results

def _search_ddgs(query):
    from ddgs import DDGS
    return list(DDGS().text(query, max_results=5))

def run_search(query):
    try:
        if TAVILY_API_KEY:
            results = _search_tavily(query)
        else:
            results = _search_ddgs(query)
        return json.dumps(results)
    except Exception as e:
        return json.dumps({"error": str(e)})

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(run_search(sys.argv[1]))
    else:
        print(json.dumps({"error": "No query provided"}))
