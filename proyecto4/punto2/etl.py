# Proyecto 4
# Computacion en la Nube
# Samuel Perez
from sqlalchemy import create_engine
from sqlalchemy import exc
import pandas as pd

# EXTRACT and TRANSFORM
df = pd.read_json('https://www.datos.gov.co/resource/2x55-9wxm.json')
df.estu_fechanacimiento = pd.to_datetime(df.estu_fechanacimiento, errors = 'raise')

# LOAD (can take a few minutes)
try:
    engine = create_engine("postgresql+psycopg2://postgres:postgressam@dbproy4.ca5eltzpchaz.us-east-1.rds.amazonaws.com:5432/dbproy4")
    print("Connected to dbproy4 \n")
    
    df.to_sql('saberpro_2019_2', con=engine, if_exists='replace')

except (Exception, exc.SQLAlchemyError) as error:
    print("\nError in connection")

finally:
    print("\nEnd")