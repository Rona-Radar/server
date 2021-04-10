from datetime import datetime

class Article:
  """Representation of a new york times article
  
  Fields
  -----
  title : str
    name of the article
  url : str
    url of the article
  byline : str
    byline of the article
  published_date : Date
    date the article was published
  thumbnail : str
    link to image thumbnail of the article
  """
  def __init__(self, title: str, url: str, abstract : str, byline: str, published_date: str, thumbnail:str):
    self.title = title
    self.url = url
    self.abstract = abstract
    self.byline = byline
    # YYYY-MM-DDThh:mm:ssTZD
    self.published_date = datetime.strptime(published_date, "%Y-%m-%dT%H:%M:%S%z")
    self.thumbnail = thumbnail
  
  def to_dict(self):
    return {
      "title": self.title,
      "url": self.url,
      "abstract": self.abstract,
      "byline": self.byline,
      "published_date": datetime.strftime(self.published_date, "%Y-%m-%dT%H:%M:%S%z"),
      "thumbnail": self.thumbnail,
    }