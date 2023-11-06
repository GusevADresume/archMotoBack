from pydantic import BaseModel
from datetime import date
from typing import List

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, ForeignKey, Text

metadata = MetaData()

text_and_img_carousel = Table(
    "text_and_img_carousel",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('page', String, nullable=False),
    Column('header', String, nullable=False),
    Column('header_text', String, nullable=False),
    Column('text', String, nullable=False),
    Column("url", String, nullable=False)
)

big_carousel = Table(
    "big_carousel",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('page', String, nullable=False),
    Column('url', String, nullable=False),
)

moto_carousel = Table(
    "moto_carousel",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('group_id', String, nullable=False),
    Column('prev_img', String, nullable=True),
    Column('url', String, nullable=False),
)

news = Table(
    "news",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('type', String, nullable=False),
    Column('video_url', String, nullable=True),
    Column('main_img_url', String, nullable=False),
    Column('text', Text, nullable=False),
    Column('header', Text, nullable=False),
    Column('road_map', Text, nullable=False),
)

news_imgs = Table(
    'news_imgs',
    metadata,
    Column('news_id', ForeignKey('news.id')),
    Column('id', Integer, primary_key=True),
    Column('url', String, nullable=False)
)

interested = Table(
    'interested',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('last_name', String, nullable=True),
    Column('country', String, nullable=True),
    Column('mail', String, nullable=True),
    Column('phone', String, nullable=True),
    Column('inquiry', String, nullable=True),
    Column('receive', String, nullable=True),
)

fan = Table(
    'fan',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('last_name', String, nullable=True),
    Column('country', String, nullable=True),
    Column('mail', String, nullable=True),
)

established = Table(
    'established',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('last_name', String, nullable=True),
    Column('country', String, nullable=True),
    Column('mail', String, nullable=True),
    Column('phone', String, nullable=True),
    Column('company_name', String, nullable=True),
    Column('business_address', String, nullable=True),
    Column('business_do', String, nullable=True),
    Column('brands', String, nullable=True),
    Column('further_information', String, nullable=True),
    Column('receive', String, nullable=True),
)

represent = Table(
    'represent',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=True),
    Column('last_name', String, nullable=True),
    Column('country', String, nullable=True),
    Column('mail', String, nullable=True),
    Column('company_name', String, nullable=True),
    Column('business_address', String, nullable=True),
    Column('products_proposing', String, nullable=True),
    Column('receive', String, nullable=True),
)

gallery = Table(
    "gallery",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('url', String, nullable=False),
    Column('page', String, nullable=False),

)

keySpec = Table(
    "keySpec",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('Displacement (cc)', String, nullable=False),
    Column('Dry Weight (lbs.)', String, nullable=False),
    Column('Torque (ftlb @ RPM)', String, nullable=False),
    Column('Tank Capacity (Gallons US)', String, nullable=False),
    Column('page', String, nullable=True),
)

specData = Table(
    "specData",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('Engine', String, nullable=False),
    Column('Displacement', String, nullable=False),
    Column('Drivetrain', String, nullable=False),
    Column('Chassis', String, nullable=False),
    Column('FrontSuspension', String, nullable=False),
    Column('RearSuspension', String, nullable=False),
    Column('FrontBrakes', String, nullable=False),
    Column('RearBrakes', String, nullable=False),
    Column('ABS', String, nullable=False),
    Column('FrontWheel', String, nullable=False),
    Column('RearWheel', String, nullable=False),
    Column('FrontTire', String, nullable=False),
    Column('FootControls', String, nullable=False),
    Column('page', String, nullable=True),
)
