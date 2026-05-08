from fastapi import FastAPI
from fastapi.responses import FileResponse

from utils.wireguard import generate_wireguard_keys
from utils.config_generator import generate_client_config

app = FastAPI()


@app.get("/")
def root():
    return {"message": "VPN API running"}


@app.get("/generate-keys")
def generate_keys():
    return generate_wireguard_keys()


@app.get("/generate-config")
def generate_config():
    keys = generate_wireguard_keys()

    config = generate_client_config(
        client_private_key=keys["private_key"],
        server_public_key="SERVER_PUBLIC_KEY",
        client_ip="10.0.0.2/32",
        server_endpoint="1.2.3.4:51820"
    )

    return {
        "config": config
    }


@app.get("/download-config")
def download_config():
    keys = generate_wireguard_keys()

    config = generate_client_config(
        client_private_key=keys["private_key"],
        server_public_key="SERVER_PUBLIC_KEY",
        client_ip="10.0.0.2/32",
        server_endpoint="1.2.3.4:51820"
    )

    file_path = "configs/client.conf"

    with open(file_path, "w") as file:
        file.write(config)

    return FileResponse(
        path=file_path,
        filename="client.conf",
        media_type="text/plain"
    )