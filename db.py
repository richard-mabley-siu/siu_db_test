from sqlalchemy.engine import create_engine
import os
import platform

#for running in windows, you MUST install Oracle Instant Client and set an environmental variable 
#called ORACLE_INSTANT_CLIENT_PATH with the location of the client (ie C:\oracle\instantclient_23_5)
#you will need to log out and log in to windows afterwards!
# https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html
# https://www.computerhope.com/issues/ch000549.htm#windows10

#for linux, add ' LD_LIBRARY_PATH="/usr/lib/oracle/19.25/client64/lib '  to your  ~/.bash_profile or  ~/.bashrc file.  you may need to logout/login and kill
#old terminals.'

def connect_oracle(host_name, service_name, username, password, port):
    print(f"Oracle Instant Client Path: {os.getenv('ORACLE_INSTANT_CLIENT_PATH')}")
    if platform.system() == 'Windows':
        oracle_instant_client_path = os.getenv('ORACLE_INSTANT_CLIENT_PATH')
        if oracle_instant_client_path:
            thick_mode = {"lib_dir" : oracle_instant_client_path}
        else:
            raise Exception('You must set an environmental variable called ORACLE_INSTANT_CLIENT_PATH.  See comments on db.py for more info.')
    else: #Linux
        oracle_instant_client_path = os.getenv('LD_LIBRARY_PATH')
        if oracle_instant_client_path:
            thick_mode = {}
        else: 
            raise Exception('You must set an environmental variable called LD_LIBRARY_PATH in your ~/.bash_profile or ~/.bashrc file.  See comments on db.py for more info.')
    #print(thick_mode)
    DIALECT = 'oracle'
    SQL_DRIVER = 'oracledb'
    USERNAME = username
    PASSWORD = password
    HOST = host_name
    PORT = port
    SERVICE = service_name
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE
    engine = create_engine(ENGINE_PATH_WIN_AUTH, thick_mode=thick_mode)

    return engine

