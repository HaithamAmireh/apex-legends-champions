import os
from dotenv import load_dotenv
from supabase.client import create_client
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "All Legends",
        "description": "Returns all legends data",
    },
    {
        "name": "Single Legend",
        "description": "Returns one legend data",
    },
    {
        "name": "Group By Class",
        "description": "Returns the Legends that fall under the same class",
    },
]


app = FastAPI(
    title="Apex Legends API",
    description="API for Apex Legends Champions Information",
    contact={
        "name": "Haitham Amireh",
        "email": "haithamamireh@gmail.com",
    },
    openapi_tags=tags_metadata,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)


class LegendData(BaseModel):
    alias: str
    quote: str
    wiki: str
    realname: str
    age: int
    homeworld: str
    class_: str
    classpassive: str
    tactical: str
    tacticalwiki: str
    passive: str
    passivewiki: str
    ultimate: str
    ultimatewiki: str


load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url or "", key or "")


@app.get('/getLegendData', tags=["All Legends"])
async def getLegendsData():
    response = supabase.table('legends').select("*").execute()
    return response

@app.get("/getLegend/{alias}", tags=["Single Legend"])
async def getLegend(alias: str):
    response = supabase.table("legends").select("*").eq("alias", alias).execute()
    return response
    
@app.get("/getClass/{class_}", tags=["Group By Class"])
async def getClass(class_: str):
    response = supabase.table("legends").select("*").eq("class", class_).execute()
    return response

@app.post('/addLegend', include_in_schema=False)
async def addLegend(legendData: LegendData):
    data = legendData.model_dump()
    existingData = (supabase.table('legends').select(
        "*").execute()).model_dump()
    if data["alias"] in existingData:
        return {"Message:": "Legend already added"}
    supabase.table('legends').insert({
        "alias": data["alias"],
        "quote": data["quote"],
        "wiki": data["wiki"],
        "real-name": data["realname"],
        "age": data["age"],
        "home-world": data["homeworld"],
        "class": data["class_"],
        "class-passive": data["classpassive"],
        "tactical": data["tactical"],
        "tactical-wiki": data["tacticalwiki"],
        "passive": data["passive"],
        "passive-wiki": data["passivewiki"],
        "ultimate": data["ultimate"],
        "ultimate-wiki": data["ultimatewiki"],
    }).execute()
    return legendData
