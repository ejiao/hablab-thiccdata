from sqlalchemy import Column, BigInteger, String, TIMESTAMP
from sqlalchemy.orm import relationship

from . import Base
# from .menuPage import MenuPage


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(BigInteger, primary_key=True)
    name = Column(String)
    sponsor = Column(String)
    event = Column(String)
    venue = Column(String)
    place = Column(String)
    physical_description = Column(String)
    occasion = Column(String)
    notes = Column(String)
    call_number = Column(String)
    keywords = Column(String)
    language = Column(String)
    date = Column(TIMESTAMP)
    location = Column(String)
    location_type = Column(String)
    currency = Column(String)
    currency_symbol = Column(String)
    status = Column(String)
    page_count = Column(BigInteger)
    dish_count = Column(BigInteger)

    menu_page = relationship("MenuPage", back_populates="menu")
