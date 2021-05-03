import os
import pandas as pd
import sqlalchemy

str_connection = 'sqlite:///{path}'

# File location
BASE_DIR = os.path.dirname( os.path.dirname( os.path.abspath(__file__)))
DATA_DIR = os.path.join( BASE_DIR, 'data')

# Finding the data
files_names = [i for i in os.listdir( DATA_DIR) if i.endswith('.csv')]

# Opening Connection
str_connection = str_connection.format(path=os.path.join(DATA_DIR, 'phones.db' ))
connection = sqlalchemy.create_engine( str_connection)


# Database insertion
for i in files_names:
    df_tmp = pd.read_csv( os.path.join(DATA_DIR, i ) )
    print(df_tmp)
    table_name = "tb_" + i.strip(".csv")
    df_tmp.to_sql(table_name, connection, if_exists='replace', index=False)


