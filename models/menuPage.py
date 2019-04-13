from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger
from sqlalchemy.orm import relationship

from . import Base
from .menu import Menu
# from .menuItem import MenuItem


class MenuPage(Base):
    __tablename__ = 'menuPage'
    id = Column(Integer, primary_key=True)
    page_number = Column(BigInteger)
    image_id = Column(BigInteger)
    full_height = Column(BigInteger)
    full_width = Column(BigInteger)
    uuid = Column(String)

    menu_id = Column(Integer, ForeignKey('menu.id'))
    menu = relationship("Menu", order_by=Menu.id, back_populates="menu_page")

    menu_item = relationship("MenuItem", back_populates="menu_page")
