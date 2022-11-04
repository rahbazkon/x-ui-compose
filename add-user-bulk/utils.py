import socket
import contextlib
import requests_toolbelt 
import requests 
import dotenv
import os
import json
import uuid
import urllib3


dotenv.load_dotenv()

server_name = os.environ.get('SERVER_NAME')
domain = os.environ.get('DOMAIN')
ssl_public_key = os.environ.get('SSL_PUBLIC_KEY')
ssl_private_key = os.environ.get('SSL_PRIVATE_KEY')
panel_username = os.environ.get('PANEL_USERNAME')
panel_password = os.environ.get('PANEL_PASSWORD')
panel_url = os.environ.get('PANEL_URL')


def is_port_open(port, host='127.0.0.1'):
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((host, port)) == 0:
            return False
        else:
            return True

def login(panel_url, panel_username, panel_password):
    with requests.session() as c:
        login_response = c.post(
            f'{panel_url}/login',
            data={
                'username': panel_username,
                'password': panel_password
            },
            headers={
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
        )
    try:    
        return login_response.headers['Set-Cookie'].split(";")[0]
    except KeyError as err:
        print('could not get session cookie')
        return None

def get_port():
    while True:
        sock = socket.socket()
        sock.bind(('', 0))
        port = sock.getsockname()[1]
        sock.close()
        if is_port_open(port):
            return port
        
def add_user(username, traffic, session_cookie):
    total = traffic * 1024 * 1024 * 1024 # convert GB to B
    remark = f'{username}@{server_name}'
    enable = True
    expiry_time = 0
    listen = ""
    port = get_port()
    protocol = 'vmess'
    settings = json.dumps({
        "clients": [
            {
                "id": str(uuid.uuid4()),
                "alterId": 0
            }
        ],
        "disableInsecureEncryption": True
    })
    stream_settings = json.dumps({
        "network":"ws",
        "security":"tls",
        "tlsSettings": {
            "serverName": domain,
            "certificates": [
                {
                    "certificateFile": ssl_public_key,
                    "keyFile": ssl_private_key
                }
            ],
            "alpn": []
        },
        "wsSettings": {
            "acceptProxyProtocol": False,
            "path": "/api",
            "headers": {}
        }
    })
    sniffing = json.dumps({
        "enabled": True,
        "destOverride":[
            "http",
            "tls"
        ]
    })

    payload = {
        "up": 0,
        "down": 0,
        "total": total,
        "remark": remark,
        "enable": enable,
        "expiryTime": expiry_time,
        "listen": listen,
        "port": port,
        "protocol": protocol,
        "settings": settings,
        "streamSettings": stream_settings,
        "sniffing": sniffing,
    }

    headers={
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': session_cookie
    }

    res = requests.post(
        f'{panel_url}/xui/inbound/add',
        headers=headers,
        json=payload
    ) 
    
    print(res)



