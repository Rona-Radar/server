from article import Article

import os
from typing import Dict, List
from aiohttp import ClientSession

class NoTokenException(Exception):
  pass

if os.path.exists("token.txt"):
  api_key = open("token.txt", "r").read()
elif "NYT_API_KEY" in os.environ:
  api_key = os.environ["NYT_API_KEY"]
else:
  raise NoTokenException("No token found")

top_health_articles_endpoint = "https://api.nytimes.com/svc/topstories/v2/health.json?api-key=" + api_key

async def fetch_health_articles():
  async with ClientSession() as session:
    async with session.get(top_health_articles_endpoint) as response:
      return await response.json()

def get_covid_health_articles(health_articles: Dict[str, any]) -> List[Article]:
  articles = []
  for article in health_articles["results"]:
    if any(["Coronavirus (2019-nCoV)" in article["des_facet"],
    "Vaccination and Immunization" in article["des_facet"]]):
      articles.append(Article(
        article["title"], 
        article["url"], 
        article["abstract"],
        article["byline"],
        article["published_date"],
        article["multimedia"][2]["url"]))
  return articles
