from models import initialize_sql
from models.menu import Menu
from models.dish import Dish
from models.menuPage import MenuPage
from models.menuItem import MenuItem
from sqlalchemy import create_engine


engine = create_engine('postgresql+psycopg2://thiccdata:hablab@localhost/menus', echo=False)
session = initialize_sql(engine)

session.query(Dish).all()