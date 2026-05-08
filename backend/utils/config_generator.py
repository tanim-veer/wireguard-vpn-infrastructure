def generate_client_config(
    client_private_key,
    server_public_key,
    client_ip,
    server_endpoint
):
    config = f"""
[Interface]
PrivateKey = {client_private_key}
Address = {client_ip}
DNS = 1.1.1.1

[Peer]
PublicKey = {server_public_key}
Endpoint = {server_endpoint}
AllowedIPs = 0.0.0.0/0
PersistentKeepalive = 25
"""

    return config