import csv
import dateparser
import os

from tqdm import tqdm
from sqlalchemy import create_engine
from models import initialize_sql
from models.menu import Menu
from models.menuItem import MenuItem
from models.menuPage import MenuPage
from models.dish import Dish

# FIRST SET UP POSTGRES:
# CREATE DATABASE menus;
# CREATE USER thiccdata WITH PASSWORD 'hablab';
# GRANT ALL PRIVILEGES ON DATABASE menus TO thiccdata;

engine = create_engine('postgresql+psycopg2://thiccdata:hablab@localhost/menus', echo=False)
session = initialize_sql(engine)

data_path = '/Users/grant/Documents/hablab-thiccdata/raw_data'

with open(os.path.join(data_path, "Menu.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    iteration = 0
    for line in tqdm(reader):
        m = session.query(Menu).filter(Menu.id == line[0]).all()
        if len(m) == 0:
            iteration += 1
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
            session.commit()

        # if iteration > 1000:
        #     session.commit()
        #     iteration = 0

session.commit()

with open(os.path.join(data_path, "MenuPage.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    iteration = 0
    for line in tqdm(reader):
        # allow for restarts
        m = session.query(MenuPage).filter(MenuPage.id == line[0]).all()

        if len(m) == 0:
            iteration += 1
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
            session.add(menu_page)

        if iteration > 1000:
            session.commit()
            iteration = 0

session.commit()

with open(os.path.join(data_path, "Dish.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    iteration = 0
    for line in tqdm(reader):
        m = session.query(Dish).filter(Dish.id == line[0]).all()
        if len(m) == 0:
            iteration += 1

            menus_appeared = line[3]
            if menus_appeared == '':
                menus_appeared = 0

            times_appeared = line[4]
            if times_appeared == '':
                times_appeared = 0

            lowest_price = line[7]
            if lowest_price == '':
                lowest_price = 0

            highest_price = line[8]
            if highest_price == '':
                highest_price = 0



            dish = Dish(
                id=line[0],
                name=line[1],
                description=line[2],
                menus_appeared=menus_appeared,
                times_appeared=times_appeared,
                first_appeared=dateparser.parse(line[5]),
                last_appeared=dateparser.parse(line[6]),
                lowest_price=lowest_price,
                highest_price=highest_price,
            )
            session.add(dish)

        if iteration > 1000:
            session.commit()
            iteration = 0

session.commit()

with open(os.path.join(data_path, "MenuItem.csv"), "r") as f:
    reader = csv.reader(f, delimiter=",")
    next(reader)
    iteration = 0
    for line in tqdm(reader):
        m = session.query(MenuPage).filter(MenuPage.id == line[0]).all()
        if len(m) == 0:
            iteration += 1
            menu_page = session.query(MenuPage).filter(MenuPage.id == line[1]).first()
            dish = session.query(Dish).filter(Dish.id == line[4]).first()

            price = line[2]
            if price == '':
                price = 0

            high_price = line[3]
            if high_price == '':
                high_price = 0

            menu_item = MenuItem(
                id=line[0],
                menu_page_id=line[1],
                price=price,
                high_price=high_price,
                dish_id=line[4],
                created_at=dateparser.parse(line[5]),
                updated_at=dateparser.parse(line[6]),
                xpos=line[7],
                ypos=line[8],

                dish=dish,
                menu_page=menu_page,
            )
            session.add(menu_item)

        if iteration > 1000:
            session.commit()
            iteration = 0

session.commit()
