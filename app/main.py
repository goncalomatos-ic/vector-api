from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.config import Config
import databases
import sqlalchemy

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

cards = sqlalchemy.Table(
    "cards",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("type", sqlalchemy.String),
    sqlalchemy.Column("position", sqlalchemy.Integer),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime),
    sqlalchemy.Column("updated_at", sqlalchemy.DateTime),
)

database = databases.Database(DATABASE_URL)

async def list_cards(request):
    query = cards.select()
    results = await database.fetch_all(query)
    content = [
        {
            "title": result["title"],
            "type": result["type"],
            "position": result["position"]
        }
        for result in results
    ]
    return JSONResponse(content)

async def update_cards(request):
    data = await request.json()
    query = cards.update().values(
       title=data["title"],
       type=data["type"]
    )
    query = cards.insert().values(title=data["title"], type=data["type"], position=data["position"])
    query = query.on_conflict_do_update(
      iconstraint='position',
      set_=dict(data=data)
    )

    await database.execute(query)
    return JSONResponse({
        "text": data["text"],
        "completed": data["completed"]
    })

routes = [
    Route("/cards", endpoint=list_cards, methods=["GET"]),
    Route("/cards", endpoint=update_cards, methods=["PATCH"]),
]

app = Starlette(
    routes=routes,
    on_startup=[database.connect],
    on_shutdown=[database.disconnect]
)