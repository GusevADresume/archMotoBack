from fastapi import FastAPI, Body, Header
from schemas import text_and_img_carousel, big_carousel, moto_carousel, news, news_imgs, interested, fan, established, \
    represent, keySpec, specData
from config import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware


#uvicorn main:app

engine = create_engine(
    DB_URL
)
engine.connect()
session = Session(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)



@app.get("/text_and_img_carousel/{page}")
async def text_and_img(page: str):
    result = [r._asdict() for r in
              session.query(text_and_img_carousel).filter(text_and_img_carousel.columns.page == page)]
    format_data = []
    items = []
    format_data.append(result[0]['header'])
    for item in result:
        i = []
        i.append(item['header_text'])
        i.append(item['text'])
        i.append(item['url'])
        items.append(i)
    format_data.append(items)
    return format_data


@app.get("/big_carousel/{page}")
async def big_car(page: str):
    result = [r._asdict() for r in
              session.query(big_carousel).filter(big_carousel.columns.page == '1S')]
    format_data = []
    for i in result:
        format_data.append(i['url'])
    return format_data


@app.get("/news_list/")
def news_list():
    result = [r._asdict() for r in
              session.query(news).all()]
    content = []
    for i in result:
        item_dict = {}
        item_dict['type'] = i['type']
        item_dict['preview'] = i['main_img_url']
        item_dict['id'] = i['id']
        item_dict['header'] = i['header']
        item_dict['text'] = str(i['text'][0:110] + "...")
        content.append(item_dict)
    return content


@app.get("/moto_carousel/")
async def moto_carousel_data():
    result = [r._asdict() for r in
              session.query(moto_carousel).all()]
    return result

@app.get("/key_spec/{page}")
async def key_spec(page: str):
    result = [r._asdict() for r in
              session.query(keySpec).filter(keySpec.columns.page == page)]
    return result[0]

@app.get("/spec_data/{page}")
async def key_spec(page: str):
    result = [r._asdict() for r in
              session.query(specData).filter(specData.columns.page == page)]
    return result[0]

@app.get("/news/{id}")
async def single_news(id: int):
    result = [r._asdict() for r in
              session.query(news).filter(news.columns.id == id)]

    content = {}
    if result[0]['type'] == 'article':
        content["mainImg"] = result[0]['main_img_url']
        content["header"] = result[0]["header"]
        content["text"] = result[0]["text"]
        content["imgs"] = [r._asdict() for r in
                           session.query(news_imgs).filter(news_imgs.columns.news_id == result[0]["id"])]
        content["elementsArrang"] = result[0]["road_map"]
    if result[0]['type'] == 'video':
        content["header"] = result[0]["header"]
        content["text"] = result[0]["text"]
        content["url"] = result[0]["video_url"]

    return content

def add_to_fan(data):
    new = fan.insert().values(
        id=1,
        name=data['name'],
        last_name=data['lastName'],
        country=data['country'],
        mail=data['email']
    )
    session.execute(new)
    session.commit()

def add_to_interested(data):
    new = interested.insert().values(
        id=1,
        name=data['name'],
        last_name=data['lastName'],
        country=data['country'],
        mail=data['email'],
        phone=data['phone'],
        inquiry=str(data['inquiry']),
        receive=str(data['marketing'])
    )
    session.execute(new)
    session.commit()

def add_to_established(data):
    new = established.insert().values(
        id=1,
        name=data['name'],
        last_name=data['lastName'],
        mail=data['email'],
        phone=data['phone'],
        company_name=data['bName'],
        business_address=data['addres'],
        business_do=data['about'],
        brands=data['brands'],
        further_information=data['information'],
        receive=data['city']
    )
    session.execute(new)
    session.commit()

def add_to_represent(data):
    new = represent.insert().values(
        id=1,
        name=data['name'],
        last_name=data['lastName'],
        country=data['addres'],
        mail=data['email'],
        company_name=str(data['commState']),
        business_address=str(data['line2'],data['city'],data['region']),
        products_proposing=str(data['propos']),
        receive=str(data['privaci'])
    )
    session.execute(new)
    session.commit()

@app.post("/forms/")
async def create_form(data = Body()):
    handlers ={
        "represent":add_to_represent,
        "established":add_to_established,
        "fan":add_to_fan,
        "interested":add_to_interested,
    }
    handlers[data['formName']](data)
    return {'content': data}
