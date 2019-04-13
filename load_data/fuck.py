from tqdm import tqdm
from sqlalchemy import create_engine
from models import initialize_sql
from models.menu import Menu
from models.menuItem import MenuItem
from models.menuPage import MenuPage
from models.dish import Dish

engine = create_engine('postgresql+psycopg2://thiccdata:hablab@localhost/menus', echo=False)
session = initialize_sql(engine)

print(session.query(Menu).count())