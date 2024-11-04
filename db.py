from sqlalchemy.engine import create_engine
import oracledb

def connect_oracle(host_name, service_name, username, password):
    DIALECT = 'oracle'
    SQL_DRIVER = 'oracledb'
    USERNAME = username #enter your username
    PASSWORD = password #enter your password
    HOST = host_name #enter the oracle db host url
    PORT = 1521 # enter the oracle port number
    SERVICE = service_name # enter the oracle db service name
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
    #print(ENGINE_PATH_WIN_AUTH)
    engine = create_engine(ENGINE_PATH_WIN_AUTH)

    return engine

