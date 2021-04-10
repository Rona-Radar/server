import asyncio
from firestore import get_articles, update_firestore
from quart import Quart, render_template, websocket
import json

app = Quart(__name__)

@app.before_serving
async def startup():
    loop = asyncio.get_event_loop()
    loop.create_task(update_firestore())

@app.route("/")
async def root_route():
    return json.dumps(get_articles())

