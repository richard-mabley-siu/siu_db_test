# %%
import db
import pandas as pd
import getpass

# Connect to SIS-DEV
# %%
# host = 'sisdb-test.eis.siu.edu'
# service = 'DEV.eis.siu.edu'
# user = input("Enter Username")
# pw = input("Enter Pass")
# or use an environmental variable...
# pw = os.getenv('oracle_pw')

# Connect to AIS
host = 'patch-db.siu.edu'
service = 'PCH'
port = 1541
user = 'APPS'
pw = getpass.getpass()


# %%
engine = db.connect_oracle(host_name=host, service_name = service, username= user, password=pw, port=port)

# %%
query = 'SELECT * FROM APPS.fnd_user FETCH FIRST 10 ROWS ONLY'
#test query
test_df = pd.read_sql_query(query, engine)

print(test_df)