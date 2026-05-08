from nacl.public import PrivateKey
import base64


def generate_wireguard_keys():
    # Génère clé privée
    private_key = PrivateKey.generate()

    # Génère clé publique associée
    public_key = private_key.public_key

    # Convertit en base64 (format WireGuard)
    private_key_b64 = base64.b64encode(bytes(private_key)).decode()
    public_key_b64 = base64.b64encode(bytes(public_key)).decode()

    return {
        "private_key": private_key_b64,
        "public_key": public_key_b64
    }