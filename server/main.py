from utils import fetch_health_articles
from quart import Quart, render_template, websocket
import asyncio

app = Quart(__name__)

@app.before_serving
async def startup():
    loop = asyncio.get_event_loop()
    loop.create_task()

@app.route("/")
async def root_route():
    health_articles = await fetch_health_articles()
    return health_articles

if __name__ == "__main__": 
    app.run(debug=True)
