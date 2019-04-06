# Connect to DB
from models import initialize_sql
engine = create_engine('postgresql+psycopg2://sochiatrist:hcirox@localhost/sochiatrist_data', echo=False)
session = initialize_sql(engine)
