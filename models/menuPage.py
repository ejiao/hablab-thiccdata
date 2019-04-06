from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from . import Base
# from .participant import Participant


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    menu_id = Column(Integer)
    page_number = Column(Integer)
    image_id = Column(Integer)
    full_height = Column(Integer)
    full_width = Column(Integer)
    uuid = Column(UUID)
