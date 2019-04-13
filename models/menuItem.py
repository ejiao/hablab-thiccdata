from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, ForeignKey
from sqlalchemy.orm import relationship

from . import Base
from .dish import Dish
from .menuPage import MenuPage


class MenuItem(Base):
    __tablename__ = 'menuItem'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    high_price = Column(Float)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)
    xpos = Column(Float)
    ypos = Column(Float)

    dish_id = Column(Integer, ForeignKey('dish.id'))
    dish = relationship("Dish", order_by=Dish.id, back_populates="menu_item")

    menu_page_id = Column(Integer, ForeignKey('menuPage.id'))
    menu_page = relationship("MenuPage", back_populates="menu_item")
