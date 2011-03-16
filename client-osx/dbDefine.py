#!/usr/bin/env python


from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

engine = create_engine('sqlite:////Users/seungjin/Documents/mydropbox/db.sqlite',echo=True)
metadata = MetaData()

event_logs_table = Table('event_logs',metadata,
  Colume('uuid',String,primary_key=True),
  Colume('mask'),
  Colume('cookie'),
  Colume('name'),
  Colume('timestamp',DateTime)
)