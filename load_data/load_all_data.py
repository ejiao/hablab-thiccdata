import csv
import dateparser
import os

from sqlalchemy import create_engine
from models import initialize_sql
from models.menu import Menu
from models.menuItem import MenuItem
from models.menuPage import MenuPage
from models.dish import Dish

# FIRST SET UP POSTGRES:
# CREATE DATABASE menus;
# CREATE USER thiccdata WITH PASSWORD 'hablab';
# GRANT ALL PRIVILEGES ON menus TO thiccdata;

engine = create_engine('postgresql+psycopg2://thiccdata:hablab@localhost/menus', echo=False)
session = initialize_sql(engine)

data_path = '/Users/grant/Documents/hablab-thiccdata/raw_data'

with open(os.path.join(data_path, "Menu.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for line in reader:
        menu = Menu(
            id=line[0],
            name=line[1],
            sponsor=line[2],
            event=line[3],
            venue=line[4],
            place=line[5],
            physical_description=line[6],
            occasion=line[7],
            notes=line[8],
            call_number=line[9],
            keywords=line[10],
            language=line[11],
            date=dateparser.parse(line[12]),
            location=line[13],
            location_type=line[14],
            currency=line[15],
            currency_symbol=line[16],
            status=line[17],
            page_count=line[18],
            dish_count=line[19],
        )
        session.add(menu)

with open(os.path.join(data_path, "MenuPage.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for line in reader:
        menu = session.query(Menu).filter(Menu.id == line[1]).first()

        menu_page = MenuPage(
            id=line[0],
            menu_id=line[1],
            page_number=line[2],
            image_id=line[3],
            full_height=line[4],
            full_width=line[5],
            uuid=line[6],

            menu=menu,
        )


with open(os.path.join(data_path, "Dish.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for line in reader:
        dish = Dish(
            id=line[0],
            name=line[1],
            description=line[2],
            menus_appeared=line[3],
            times_appeared=line[4],
            first_appeared=dateparser.parse(line[5]),
            last_appeared=dateparser.parse(line[6]),
            lowest_price=line[7],
            highest_price=line[8],
        )

with open(os.path.join(data_path, "MenuItem.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    for line in reader:
        menu_page = session.query(MenuPage).filter(MenuPage.id == line[1]).first()
        dish = session.query(Dish).filter(Dish.id == line[4]).first()

        menu_item = MenuItem(
            id=line[0],
            menu_page_id=line[1],
            price=line[2],
            high_price=line[3],
            dish_id=line[4],
            created_at=dateparser.parse(line[5]),
            updated_at=dateparser.parse(line[6]),
            xpos=line[7],
            ypos=line[8],

            dish=dish,
            menu_page=menu_page,
        )

session.commit()
