from sqlalchemy import Column, String
from sql import *


class fban(BASE):
    __tablename__ = "channels"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


fban.__table__.create(checkfirst=True)


def in_channels(chat_id):
    try:
        return SESSION.query(fban).filter(fban.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_channel(chat_id):
    adder = fban(str(chat_id))
    SESSION.add(adder)
    SESSION.commit()


def rm_channel(chat_id):
    rem = SESSION.query(fban).get(str(chat_id))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()


def get_all_channels():
    rem = SESSION.query(fban).all()
    SESSION.close()
    return rem
