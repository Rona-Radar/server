import asyncio
import os
from typing import Dict
from aiohttp import ClientSession

api_key = open(os.path.join(os.path.dirname(__file__), os.pardir, "token.txt"), "r").read()
top_health_articles_endpoint = "https://api.nytimes.com/svc/topstories/v2/health.json?api-key=" + api_key
print(top_health_articles_endpoint)

async def fetch_health_articles():
  async with ClientSession() as session:
    async with session.get(top_health_articles_endpoint) as response:
      return await response.json()

async def get_covid_health_articles(health_articles: Dict[str, any]):
  pass
