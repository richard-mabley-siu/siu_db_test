from sqlalchemy.engine import create_engine
import oracledb
#thick mode required for AIS connection!
#https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
thick_mode = {"lib_dir" : r"C:\oracle\instantclient_23_5"}

def connect_oracle(host_name, service_name, username, password, port):
    DIALECT = 'oracle'
    SQL_DRIVER = 'oracledb'
    USERNAME = username #enter your username
    PASSWORD = password #enter your password
    HOST = host_name #enter the oracle db host url
    PORT = port # enter the oracle port number
    SERVICE = service_name # enter the oracle db service name
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
    #print(ENGINE_PATH_WIN_AUTH)
    engine = create_engine(ENGINE_PATH_WIN_AUTH, thick_mode=thick_mode)
    #engine = create_engine(ENGINE_PATH_WIN_AUTH)

    return engine

