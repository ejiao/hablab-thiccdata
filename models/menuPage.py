from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from . import Base
from .menu import Menu
# from .menuItem import MenuItem


class MenuPage(Base):
    __tablename__ = 'menuPage'
    id = Column(Integer, primary_key=True)
    page_number = Column(Integer)
    image_id = Column(Integer)
    full_height = Column(Integer)
    full_width = Column(Integer)
    uuid = Column(String)

    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship("Menu", order_by=Menu.id, back_populates="menu_page")

    menu_item = relationship("MenuItem", back_populates="menu_page")
