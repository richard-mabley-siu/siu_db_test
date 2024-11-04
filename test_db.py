# %%
import db
import os
import pandas as pd

# %%
host = 'sisdb-test.eis.siu.edu'
service = 'DEV.eis.siu.edu'
user = input("Enter Username")
pw = input("Enter Pass")
# or use an environmental variable...
# pw = os.getenv('oracle_pw')

# %%
engine = db.connect_oracle(host_name=host, service_name = service, username= user, password=pw)

# %%
query = 'SELECT * FROM SPRIDEN FETCH FIRST 10 ROWS ONLY'
#test query
test_df = pd.read_sql_query(query, engine)

print(test_df)