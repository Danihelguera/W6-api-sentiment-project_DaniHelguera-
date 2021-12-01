import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("sql")


dbName="amazon_rating"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)

