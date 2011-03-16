#!/usr/bin/env python


import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


class database :
  
  def __init__(self):
    engine = create_engine('sqlite:////Users/seungjin/Documents/mydropbox/db.sqlite',echo=True)
    metadata = MetaData()
    event_logs_table = Table('event_logs',metadata,
      Colume('uuid',String,primary_key=True),
      Colume('mask'),
      Colume('cookie'),
      Colume('name'),
      Colume('timestamp',DateTime)
    )



