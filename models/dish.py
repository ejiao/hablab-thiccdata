from sqlalchemy import Column, Integer, Float, String, TIMESTAMP
from sqlalchemy.orm import relationship

from . import Base
# from .menuItem import MenuItem


class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    menus_appeared = Column(Integer)
    times_appeared = Column(Integer)
    first_appeared = Column(TIMESTAMP)
    last_appeared = Column(TIMESTAMP)
    lowest_price = Column(Float)
    highest_price = Column(Float)

    menu_item = relationship("MenuItem", back_populates="dish")
