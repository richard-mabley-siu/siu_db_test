from sqlalchemy.engine import create_engine
import oracledb
import os
import platform

#for running in windows, you MUST install Oracle Instant Client and set an environmental variable 
#called ORACLE_INSTANT_CLIENT_PATH with the location of the client (ie C:\oracle\instantclient_23_5)
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# https://www.computerhope.com/issues/ch000549.htm#windows10

def connect_oracle(host_name, service_name, username, password, port):
    if platform.system() == 'Windows':
        oracle_instant_client_path = os.getenv('ORACLE_INSTANT_CLIENT_PATH')
        if oracle_instant_client_path != '':
            thick_mode = {"lib_dir" : oracle_instant_client_path}
        else:
            raise Exception('You must set an environmental variable called ORACLE_INSTANT_CLIENT_PATH.  See comments on db.py for more info.')
    else:
        thick_mode = {}

    DIALECT = 'oracle'
    SQL_DRIVER = 'oracledb'
    USERNAME = username #enter your username
    PASSWORD = password #enter your password
    HOST = host_name #enter the oracle db host url
    PORT = port # enter the oracle port number
    SERVICE = service_name # enter the oracle db service name
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
    engine = create_engine(ENGINE_PATH_WIN_AUTH, thick_mode=thick_mode)

    return engine

