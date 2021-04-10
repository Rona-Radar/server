from utils import fetch_health_articles
from quart import Quart, render_template, websocket

app = Quart(__name__)

@app.route("/")
async def root_route():
    health_articles = await fetch_health_articles()
    return health_articles

if __name__ == "__main__":
    app.run(debug=True)
