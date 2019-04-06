from sqlalchemy import Column, Integer, Double, String, TIMESTAMP
from sqlalchemy.orm import relationship

from . import Base
# from .participant import Participant


class Dish(Base):
    __tablename__ = 'dish'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    menus_appeared = Column(Integer)
    times_appeared = Column(Integer)
    first_appeared = Column(TIMESTAMP)
    last_appeared = Column(TIMESTAMP)
    lowest_price = Column(Double)
    highest_price = Column(Double)


    # participant = relationship("Participant", order_by=Participant.id, back_populates="study")
    #
    # def __repr__(self):
    #     return "Study: %s\nDescription: %s\nDate Created: %s\nDate Updated: %s\n" % (
    #         self.name,
    #         self.description,
    #         str(self.date_created),
    #         str(self.last_updated),
    #     )
