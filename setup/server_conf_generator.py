import base64
import json

def decode_vmess(vmess_config):
    # Decode the base64-encoded Vmess configuration
    decoded_vmess = base64.b64decode(vmess_config).decode('utf-8')

    # Parse the JSON content
    vmess_json = json.loads(decoded_vmess)

    return vmess_json

# Vmess configuration
vmess_config = input("Please enter your vmess config: ")

if len(vmess_config.split('vmess://')) !=  2:
    print("Invalid vmess config")
    exit(1)

vmess_config = vmess_config.split('vmess://')[1]

# Decode Vmess configuration
try:
    decoded_vmess_json = decode_vmess(vmess_config)
except:
    print("Invalid vmess config: Error in decoding the config")
    exit(1)

if 'arvan' in decoded_vmess_json['sni']:
    sniPattern = 'apps.' + decoded_vmess_json['sni'].split('.apps.')[1]
elif 'darkube' in decoded_vmess_json['sni']:
    sniPattern = 'darkube.' + decoded_vmess_json['sni'].split('.darkube.')[1]
else:
    print("Unhandled sniPattern")
    exit(1)

print(decoded_vmess_json)

try:
    server_conf = {
        "name": input("Please enter a name for your server: "),
        "url": input("Please enter the url of xui server ending with /qpcmck: "),
        "username": input("Enter username of the xui: "),
        "password": input("Enter password of the xui: "),
        "httpAuth": input("Enter the basic token of the nginx in the: "),
        "AcceptingNew": input("Accepting new (Y/N)?: ").lower() == 'y',
        "org": input("Enter the org name: "),
        "rowRemark": input("Enter name of the rowRemark in xui: "),
        "clientPort": int(decoded_vmess_json['port']),
        "domain": decoded_vmess_json['add'],
        "SNIPattern": sniPattern,
        "traffic": int(input("Enter the default traffic (Recommended default is 20): ")),
        "tls": decoded_vmess_json['tls'] == 'tls',
        "path": decoded_vmess_json['path'],
        "note": "abr-ham-de",
        "isActive": True
    }
except:
    print("Error in parsing the config")
    exit(1)

print("==========================")
print(json.dumps(server_conf, indent=2))
print("==========================")
