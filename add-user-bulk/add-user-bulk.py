import pandas as pd
import os
import uuid
import requests 
import utils
import dotenv
import json

dotenv.load_dotenv()

server_name = os.environ.get('SERVER_NAME', None)
domain = os.environ.get('DOMAIN', None)
ssl_public_key = os.environ.get('SSL_PUBLIC_KEY', None)
ssl_private_key = os.environ.get('SSL_PRIVATE_KEY', None)
panel_username = os.environ.get('PANEL_USERNAME', None)
panel_password = os.environ.get('PANEL_PASSWORD', None)
panel_url = os.environ.get('PANEL_URL', None)

if server_name is None:
    print("please provide valid SERVER_NAME env")
    exit(0) 

if domain is None:
    print("please provide valid DOMAIN env")
    exit(0)

if ssl_public_key is None:
    print("please provide valid SSL_PUBLIC_KEY env")
    exit(0)

if ssl_private_key is None:
    print("please provide valid SSL_PRIVATE_KEY env")
    exit(0)

if panel_username is None:
    print("please provide valid USERNAME env")
    exit(0)

if panel_password is None:
    print("please provide valid PASSWORD env")
    exit(0)

if panel_url is None:
    print("please provide valid PANEL_URL env")
    exit(0) 


users_file = pd.read_csv('./users-bulk.csv', index_col=0)

error_file = pd.DataFrame([], columns=users_file.columns)



if __name__ == "__main__":
    session_cookie = utils.login(panel_url, panel_username, panel_password)
    if session_cookie is None:
        exit(0)

    for username,row in users_file.iterrows():
        utils.add_user(username=username, traffic=row['traffic'], session_cookie=session_cookie)
        
