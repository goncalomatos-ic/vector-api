from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route
from starlette.config import Config
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from sqlalchemy.dialects.postgresql import insert
import databases
import sqlalchemy

config = Config('.env')
DATABASE_URL = config('DATABASE_URL')

metadata = sqlalchemy.MetaData()

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

# 'Upsert' a card
async def add_card(request):
  data = await request.json()
  card_info = data["data"]

  insert_stmt = insert(cards).values(title=card["title"], type=card["type"], position=card["position"])
  query = insert_stmt.on_conflict_do_update(
    index_elements=['position'],
    set_=dict(title=card["title"], type=card["type"])
  )
  await database.execute(query)

  return JSONResponse(data)

# Delete card by id
async def delete_card (request):
  card_id = request.path_params['user_id']
  delete_query = cards.delete().where(cards.c.id==card_id)
  await database.execute(delete_query)
  return JSONResponse(card_info)

# Get all cards
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

# Updates cards according to payload
# May remove, add or update existing cards
async def update_cards(request):
  data = await request.json()
  cards_info = data["data"]

  # Get cards positions (that is unique) to remove the ones
  # not included in the payload
  cards_positions = []

  # Insert or update
  for card in cards_info:
    cards_positions.append(card["position"])
    insert_stmt = insert(cards).values(title=card["title"], type=card["type"], position=card["position"])
    query = insert_stmt.on_conflict_do_update(
      index_elements=['position'],
      set_=dict(title=card["title"], type=card["type"])
    )
    await database.execute(query)

  # Delete cards that aren't on the payload
  delete_query = cards.delete().where(cards.c.position.notin_(cards_positions))
  await database.execute(delete_query)

  return JSONResponse(cards_info)

routes = [
  Route("/cards", endpoint=list_cards, methods=["GET"]),
  Route("/cards", endpoint=add_card, methods=["POST"]),
  Route("/cards/{card_id:int}", endpoint=delete_card, methods=["DELETE"]),
  Route("/cards", endpoint=update_cards, methods=["PATCH"]),
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'])
]


app = Starlette(
  routes=routes,
  middleware=middleware,
  on_startup=[database.connect],
  on_shutdown=[database.disconnect]
)