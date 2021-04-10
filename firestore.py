from google.cloud import firestore
import asyncio
import os

from article import Article
from utils import fetch_health_articles, get_covid_health_articles


db = firestore.Client()

def get_articles():
  articles = []

  articles_ref = db.collection(u'articles')
  docs = articles_ref.stream()

  for doc in docs:
    articles.append(doc.to_dict())
  return articles

async def update_firestore():
  health_artices = await fetch_health_articles()
  covid_articles = get_covid_health_articles(health_artices)

  batch = db.batch()

  old_articles_ref = db.collection(u'articles')
  for article in old_articles_ref.stream():
    batch.delete(article.reference)

  for article in covid_articles:
    batch.set(db.collection(u"articles").document(), article.to_dict())
  
  batch.commit()

  await asyncio.sleep(1800)