from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

from . import Base
# from .participant import Participant


class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
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
    currecny_symbol = Column(String)
    status = Column(String)
    page_count = Column(Integer)
    dish_count = Column(Integer)


    # participant = relationship("Participant", order_by=Participant.id, back_populates="study")
    #
    # def __repr__(self):
    #     return "Study: %s\nDescription: %s\nDate Created: %s\nDate Updated: %s\n" % (
    #         self.name,
    #         self.description,
    #         str(self.date_created),
    #         str(self.last_updated),
    #     )
